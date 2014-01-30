from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

from django.contrib.auth import authenticate, login

from rest_framework import authentication
from rest_framework import exceptions

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	"""	
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
						
					
class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
