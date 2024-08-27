from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register('events', EventViewSet)
router.register('categories', EventCategoryViewSet)
router.register('vendor', VendorViewSet, basename='vendor')

urlpatterns = router.urls
