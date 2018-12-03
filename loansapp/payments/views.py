from rest_framework import generics
from ..models import payments
from .serializers import PaymentsSerializer

class PaymentsView(generics.ListCreateAPIView):
    queryset = payments.objects.all()
    serializer_class = PaymentsSerializer