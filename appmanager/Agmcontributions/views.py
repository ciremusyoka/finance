from rest_framework import generics
from ..models import AGMContributions,AGMBalances
from .serializers import AGMContributionSerializer, AGMBalancesSerializer

class AGMCreateView(generics.ListCreateAPIView):
    queryset = AGMContributions.objects.all()
    serializer_class = AGMContributionSerializer


class AGMBalancesView(generics.ListCreateAPIView):
    queryset = AGMBalances.objects.all()
    serializer_class = AGMBalancesSerializer