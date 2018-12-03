from rest_framework import generics
from ..models import PledgePayments
from .serializers import PledgesPaymentSerializer


# create and list pledges paid
class PledgePaymentView(generics.ListCreateAPIView):
    queryset = PledgePayments.objects.all()
    serializer_class = PledgesPaymentSerializer