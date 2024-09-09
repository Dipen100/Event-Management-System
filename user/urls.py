
from django.urls import path
from .views import *

urlpatterns = [
    path('register_user/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profiles/', UserProfileListView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/me/', UserProfileDetailView.as_view(), name='my-profile'),
]