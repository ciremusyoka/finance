from django.shortcuts import render
from rest_framework import generics
from .models import AllPledges, PledgePurpose
from .serializers import AllPledgesSerializer, PledgePurposeSerializer


# create and list pledges purposes
class PledgePurposesView(generics.ListCreateAPIView):
    queryset = PledgePurpose.objects.all()
    serializer_class = PledgePurposeSerializer


# create and list pledges
class CreatePledgeView(generics.ListCreateAPIView):
    queryset = AllPledges.objects.all()
    serializer_class = AllPledgesSerializer
