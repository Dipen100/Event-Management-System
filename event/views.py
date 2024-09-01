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
    serializer_class = EventLogisticSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrEventPlannerOrReadOnly
    ]
    
class EquipmentsViewSet(viewsets.ModelViewSet):
    queryset = Equipments.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrEventPlannerOrReadOnly
    ]

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]
    
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]
    
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [
        IsAuthenticated, IsAdminOrClientOrReadOnly
    ]

# class RegisterAttendeeView(APIView):
#     def post(self, request, *args, **kwargs):
#         event_id = request.data.get('event')
#         user_id = request.data.get('user')
        
#         # Validate if event exists
#         if not Event.objects.filter(id=event_id).exists():
#             return Response({'error': 'Event does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Create or update attendee registration
#         attendee, created = Attendee.objects.get_or_create(event_id=event_id, user_id=user_id, defaults={'status': 'Registered'})
        
#         if not created:
#             return Response({'error': 'You are already registered for this event'}, status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = AttendeeSerializer(attendee)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# class CommunicationView(APIView):
#     def post(self, request, *args, **kwargs):
#         attendee_id = request.data.get('attendee')
#         message = request.data.get('message')
        
#         # Validate if attendee exists
#         if not Attendee.objects.filter(id=attendee_id).exists():
#             return Response({'error': 'Attendee does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Create communication record
#         communication = Communication.objects.create(attendee_id=attendee_id, message=message)
#         serializer = CommunicationSerializer(communication)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
