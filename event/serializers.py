from rest_framework import serializers
from .models import *

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'event_name']

class EventSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=EventCategory.objects.all(), source='category', write_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'location', 'description', 'category', 'category_id']

class VendorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), source='event', write_only=True)
    event = EventSerializer(read_only=True)
    
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'email','address', 'phone', 'event', 'event_id']

    def create(self, validated_data):
        event = validated_data.pop('event')
        
        vendor = Vendor.objects.create(event=event, **validated_data)

        return vendor

class CateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = [
            'id', 'name', 'address', 'phone'
        ]
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields = [
            'id', 'name'
        ]
        
class EventLogisticSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), source='event', write_only=True)
    
    catering_id = serializers.PrimaryKeyRelatedField(queryset=Catering.objects.all(), source='catering', write_only=True)
    
    equipment_id = serializers.PrimaryKeyRelatedField(queryset=Equipments.objects.all(), source='equipments', many=True, write_only=True)
    
    event = EventSerializer(read_only=True)
    catering = CateringSerializer(read_only=True)
    equipments = EquipmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = EventLogistics
        fields = '__all__'
        
    def create(self, validated_data):
        event = validated_data.pop('event')
        catering = validated_data.pop('catering')
        equipments = validated_data.pop('equipments')
        
        event_logistics = EventLogistics.objects.create(event=event, catering=catering, **validated_data)
        
        event_logistics.equipments.set(equipments)
        
        return event_logistics

class AttendeeSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), source='event', write_only=True)
    
    event = EventSerializer(read_only=True)

    class Meta:
        model = Attendee
        fields = [
            'id', 'name', 'address', 'phone', 'event_id', 'event'
        ]
    
    def create(self, validated_data):
        event = validated_data.pop('event')
        attendee = Attendee.objects.create(event=event, **validated_data)       
        return attendee
        
class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = ['id', 'attendee', 'sent_at', 'message']

class TicketSerializer(serializers.ModelSerializer):
    attendee_id = serializers.PrimaryKeyRelatedField(queryset=Attendee.objects.all(), source='attendee', write_only=True)
        
    attendee = AttendeeSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    ticket_id = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), source='ticket', write_only=True)
        
    ticket = TicketSerializer(read_only=True)
    
    class Meta:
        model = Reservation
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    ticket_id = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), source='ticket', write_only=True)
        
    ticket = TicketSerializer(read_only=True)
    
    class Meta:
        model = Invoice
        fields = ['id','ticket_id', 'ticket', 'is_paid', 'issued_at']

class ReceiptSerializer(serializers.ModelSerializer):
    invoice_id = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all(), source='invoice', write_only=True)
    
    invoice = InvoiceSerializer(read_only=True)
    
    class Meta:
        model = Receipt
        fields = "__all__"