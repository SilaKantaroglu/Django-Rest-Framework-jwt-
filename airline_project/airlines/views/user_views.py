from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth.models import User
from ..serializers import UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

def login_view(request):
    return render(request, 'login.html')

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
