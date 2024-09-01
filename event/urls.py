from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register('events', EventViewSet)
router.register('categories', EventCategoryViewSet)
router.register('vendor', VendorViewSet, basename='vendor')
router.register('event_logistic', EventLogisticViewSet, basename='event_logistic')
router.register('catering', CateringViewSet, basename='catering')
router.register('equipments', EquipmentsViewSet, basename='equipments')

router.register('attendees', AttendeeViewSet)
router.register('communications', CommunicationViewSet)
router.register('ticketing', TicketViewSet)
router.register('reservations', ReservationViewSet)
router.register('invoices', InvoiceViewSet)
router.register('receipt', ReceiptViewSet, basename='receipt')

urlpatterns = [
    # path('', include(router.urls)),
    # path('register_event/', RegisterAttendeeView.as_view(), name='register'),
    # path('communicate/', CommunicationView.as_view(), name='communicate'),
]+router.urls