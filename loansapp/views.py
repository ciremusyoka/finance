from django.shortcuts import render
from rest_framework import generics
from .models import loans
from .serializers import CreateLoansSerializer, ListLoanSerializer

class CreateLoansView(generics.ListCreateAPIView):
    queryset = loans.objects.all()
    serializer_class = CreateLoansSerializer

class AllLoansAndPayment(generics.ListAPIView):
    queryset = loans.objects.all()
    serializer_class = ListLoanSerializer

class LoanListView(generics.RetrieveAPIView):
    queryset = loans.objects.all()
    serializer_class = ListLoanSerializer