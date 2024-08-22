from rest_framework import serializers
from .models import Event, EventCategory

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
