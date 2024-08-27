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
        fields = ['id', 'name', 'email', 'phone', 'event', 'event_id']

    def create(self, validated_data):
        event = validated_data.pop('event')
        
        vendor = Vendor.objects.create(event=event, **validated_data)

        return vendor
