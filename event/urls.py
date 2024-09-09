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
router.register('review', ReviewViewset, basename='review')

urlpatterns = [
    
]+router.urls