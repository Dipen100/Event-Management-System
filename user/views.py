
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .permissions import *

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'role': user.role
        })

class UserProfileListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ] 

    def get(self, request, *args, **kwargs):
        '''print(request.user.role) '''
        return super().get(request, *args, **kwargs)
    
class UserProfileDetailView(generics.RetrieveAPIView):
    # queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  

    def get_object(self):
        return self.request.user
        '''if self.kwargs.get('pk') == 'me':
            return self.request.user
        return super().get_object()'''