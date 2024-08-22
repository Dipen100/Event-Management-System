from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register('events', EventViewSet)
router.register('categories', EventCategoryViewSet)

urlpatterns = router.urls
