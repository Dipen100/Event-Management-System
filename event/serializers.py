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
    
    # equipment_id = serializers.PrimaryKeyRelatedField(queryset=Equipments.objects.all(), source='equipment', write_only=True)
    
    event = EventSerializer(read_only=True)
    catering = CateringSerializer(read_only=True)
    equipment = EquipmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = EventLogistics
        fields = '__all__'
        
    def create(self, validated_data):
        # raise Exception(validated_data)
        event = validated_data.pop('event')
        catering = validated_data.pop('catering')
        equipment = validated_data.pop('equipments')
        
        event_logistics = EventLogistics.objects.create(event=event, catering=catering, **validated_data)
        
        # raise Exception(event_logistics)
        event_logistics.equipments.set(equipment)
        
        return event_logistics

