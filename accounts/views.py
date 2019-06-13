from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework import generics
from django.views import generic
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

