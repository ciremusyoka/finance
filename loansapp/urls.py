from django.urls import re_path
from .views import CreateLoansView, LoanListView, AllLoansAndPayment
from .payments.views import PaymentsView
from .interests.views import interestView

urlpatterns = [
    re_path(r'^loans$', CreateLoansView.as_view(), name='register_loans'),
    re_path(r'^loansandpay', AllLoansAndPayment.as_view(), name='loans&pay'),
    re_path(r'^loan/(?P<pk>[0-9]+)$', LoanListView.as_view(), name='View_loan'),
    re_path(r'^payments', PaymentsView.as_view(), name='register_payments'),
    re_path(r'^interests', interestView.as_view(), name='register_interests'),
]