from rest_framework import generics
from ..models import interests
from .serializers import CreateInterestSerializer

class interestView(generics.ListCreateAPIView):
    queryset = interests.objects.all()
    serializer_class = CreateInterestSerializer