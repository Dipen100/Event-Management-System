from rest_framework import viewsets, filters
from .models import Event, EventCategory
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from user.permissions import *

class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrEventPlannerOrReadOnly
    ]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated ,IsAdminOrEventPlannerOrReadOnly
    ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location', 'description']
    ordering_fields = ['date', 'title']
