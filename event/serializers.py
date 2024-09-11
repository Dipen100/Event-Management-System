from rest_framework import serializers
from .models import *

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = [
            'id',
            'event_name'
        ]

class EventSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=EventCategory.objects.all(),
        source='category',
        write_only=True
    )
    category = EventCategorySerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'date',
            'location',
            'description',
            'price',
            'category_id',
            'category',
        ]
        
class EventUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'date',
            'location',
            'description',
        ]
        
class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'category',
            'title',
            'date',
            'location',
            'description',
            'price'
        ]

class VendorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event',
        write_only=True
    )
    event = EventSerializer(read_only=True)
    
    class Meta:
        model = Vendor
        fields = [
            'id',
            'name',
            'email',
            'address',
            'phone',
            'event',
            'event_id'
        ]

    def create(self, validated_data):
        event = validated_data.pop('event')        
        vendor = Vendor.objects.create(event=event, **validated_data)
        
        return vendor

class CateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = [
            'id',
            'name',
            'address',
            'phone'
        ]
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields = [
            'id',
            'name'
        ]

# EventLogistics Part Starts Here        
class CreateEventLogisticSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event'
    )
    
    catering_id = serializers.PrimaryKeyRelatedField(
        queryset=Catering.objects.all(),
        source='catering'
    )
    
    equipment_id = serializers.PrimaryKeyRelatedField(
        queryset=Equipments.objects.all(),
        source='equipments',
        many=True
    )
    
    class Meta:
        model = EventLogistics
        fields = [
            'id',
            'event_id',
            'catering_id',
            'equipment_id',
            'transportation',
        ]
        
    def create(self, validated_data):
        equipments = validated_data.pop('equipments')
        event_logistics = EventLogistics.objects.create(**validated_data)        
        event_logistics.equipments.set(equipments)
                
        return event_logistics

class UpdateEventLogisticSerializer(serializers.ModelSerializer):  
    price = serializers.DecimalField(
        max_digits=100000,
        decimal_places=2,
        required=True
    )
  
    class Meta:
        model = EventLogistics
        fields = [
            'id',
            'event',
            'catering',
            'equipments',
            'transportation',
            'price'
        ]

class EventLogisticViewSerializer(serializers.ModelSerializer):    
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event',
        write_only=True
    )
    
    catering_id = serializers.PrimaryKeyRelatedField(
        queryset=Catering.objects.all(),
        source='catering',
        write_only=True
    )
    
    equipment_id = serializers.PrimaryKeyRelatedField(
        queryset=Equipments.objects.all(),
        source='equipments',
        many=True,
        write_only=True
    )
    
    event = EventSerializer(read_only=True)
    catering = CateringSerializer(read_only=True)
    equipments = EquipmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = EventLogistics
        fields = [
            'id',
            'event_id',
            'event',
            'catering_id',
            'catering',
            'equipment_id',
            'equipments',
            'transportation',
        ]
# EventLogistics Part End Here

class AttendeeViewSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event',
        write_only=True
    )
    
    event = EventSerializer(read_only=True)  
     
    class Meta:
        model = Attendee
        fields = [
            'client_id',
            'id',
            'name',
            'address',
            'phone',
            'event_id',
            'event',
            'registered_at',
            'message'
        ]
class AttendeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = [
            'id',
            'name',
            'address',
            'phone',
            'event',
            'registered_at',
            'message'
        ]

class EventAttendeeCreateSerializer(serializers.Serializer):
    client = serializers.HiddenField(default=serializers.CurrentUserDefault())
    event_id = serializers.IntegerField()
    attendees = AttendeeCreateSerializer(many=True)  
    
    def create(self, validated_data):
        client = self.context['request'].user
        event_id = validated_data.get('event_id')
        attendees_data = validated_data.get('attendees')
        # raise Exception(client)

        event = Event.objects.get(id=event_id)
        attendee_list = []

        for attendee_data in attendees_data:
            attendee_data.pop('event', None)
            attendee = Attendee.objects.create(
                event=event,
                client=client,
                **attendee_data
            )
            attendee_list.append(attendee)

        return attendee_list

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = [
            'id',
            'attendee',
            'sent_at',
            'message',
            'client_response'
        ]
        
class CommunicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = [
            'id',
            'attendee',
            'sent_at',
            'message'
        ]
        
class ReservedEventViewSerializer(serializers.ModelSerializer):    
    attendee_id = serializers.PrimaryKeyRelatedField(
        queryset=Attendee.objects.all(),
        source='attendee',
        write_only=True
    )
    
    attendee = AttendeeViewSerializer(read_only=True)
    
    class Meta:
        model = Reservation
        fields = [
            'id',
            'attendee_id',
            'attendee',
            'reserved_at',
            'message'
        ]

class ReserveEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'id',
            'event',
            'attendee',
            'reserved_at',
            'message'
        ]

class TicketViewSerializer(serializers.ModelSerializer):
    attendee_id = serializers.PrimaryKeyRelatedField(
        queryset=Attendee.objects.all(),
        source='attendee',
        write_only=True
    )
    
    attendee = AttendeeViewSerializer(read_only=True)
    
    class Meta:
        model = Ticket
        fields = [
            'id',
            'attendee_id',
            'attendee',
            'ticket_type',
            'ticket_number',
            'ticket_price',
            'total_price',
            'issued_at',
        ]

class TicketPurchaseSerializer(serializers.ModelSerializer):
    reservation_id = serializers.PrimaryKeyRelatedField(
        queryset=Reservation.objects.all(),
        required=False,
        allow_null=True
    )
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event',
        required=False,
        allow_null=True
    )
    attendee_id = serializers.PrimaryKeyRelatedField(
        queryset=Attendee.objects.all(),
        source='attendee',
        required=False,
        allow_null=True
    )

    class Meta:
        model = Ticket
        fields = [
            'reservation_id',
            'attendee_id',
            'event_id',
            'ticket_type',
            'ticket_number',
            'ticket_price',
            'issued_at'
        ]
     
    def validate(self, attrs):
        reservation_id = attrs.get('reservation_id', None)
        event = attrs.get('event', None)
        attendee = attrs.get('attendee', None)

        if reservation_id:
            if event or attendee:
                raise serializers.ValidationError(
                    "Event and attendee should not be provided when reservation_id is used."
                )
            
            reservation = Reservation.objects.get(id=reservation_id.id)
            attrs['event'] = reservation.event
            attrs['attendee'] = reservation.attendee
        else:
            if not event or not attendee:
                raise serializers.ValidationError(
                    "Event and attendee are required if no reservation is provided."
                )
        
        return attrs

    def create(self, validated_data):
        reservation_id = validated_data.pop('reservation_id', None)
        
        if reservation_id:
            reservation = Reservation.objects.get(id=reservation_id.id)
            validated_data['event'] = reservation.event
            validated_data['attendee'] = reservation.attendee
        else:
            validated_data['event'] = validated_data['event']
            validated_data['attendee'] = validated_data['attendee']
        
        return Ticket.objects.create(**validated_data)
        

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'id',
            # 'attendee',
            'ticket',
            'amount',
            'is_paid',
            'created_at',
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'invoice',
            'payment_mode',
            'amount_paid',
            'transaction_id',
            'payment_date'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'event',
            'attendee',
            'rating',
            'feedback',
            'created_at'
        ]
