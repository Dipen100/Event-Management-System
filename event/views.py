from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, filters
from rest_framework import status
from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from user.permissions import *
from rest_framework.views import APIView

class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrEventPlannerOrReadOnly
    ]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location', 'description']
    ordering_fields = ['date', 'title']
    permission_classes = [
        IsAuthenticated ,IsAdminOrEventPlannerOrReadOnly
    ]
    
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT':
            return EventUpdateSerializer
        
        elif method == 'POST':
            return EventCreateSerializer
        
        return EventSerializer
    
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    ordering_fields = ('id',)
    permission_classes = [
        IsAuthenticated, IsAdminOrVendorOrReadOnly
    ]

class CateringViewSet(viewsets.ModelViewSet):
    queryset = Catering.objects.all()
    serializer_class = CateringSerializer
    ordering_fields = ('id',)
    
    permission_classes = [
        IsAuthenticated, IsAdminOrEventPlannerOrReadOnly
    ]

class EventLogisticViewSet(viewsets.ModelViewSet):
    queryset = EventLogistics.objects.all()
    serializer_class = EventLogisticViewSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrEventPlannerOrReadOnly
    ]
    
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT':
            return UpdateEventLogisticSerializer
        
        if method == 'POST':
            return CreateEventLogisticSerializer
        
        return EventLogisticViewSerializer
    
class EquipmentsViewSet(viewsets.ModelViewSet):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrEventPlannerOrReadOnly
    ]

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeViewSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]
    
    def get_serializer_class(self):
        method = self.request.method
        if method == 'POST':
            return AttendeeCreateSerializer
        
        return AttendeeViewSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketViewSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TicketPurchaseSerializer
        
        return TicketViewSerializer
    
    http_method_names={
        'get', 'post', 'patch',
    }
    

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservedEventViewSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]
    
    def get_serializer_class(self):
        method = self.request.method
        if method == 'POST':
            return ReserveEventSerializer
        
        return ReservedEventViewSerializer
    
    http_method_names={
        'get', 'post', 'patch',
    }
    
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer