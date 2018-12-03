from django.shortcuts import render
from rest_framework import generics
from .models import MyUser, members

from .serializers import CreateUserSerializer, MembersSerializer

# end point for creating user
class CreateUserView(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    # permission_classes = (permissions.IsAllowany)
    serializer_class = CreateUserSerializer


# create and retrieve users
class membersView(generics.ListCreateAPIView):
    queryset = members.objects.all()
    serializer_class = MembersSerializer