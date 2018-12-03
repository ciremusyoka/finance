from django.urls import re_path
from .views import (CreateUserView, membersView)
from .Agmcontributions.views import AGMCreateView, AGMBalancesView

urlpatterns = [
    re_path(r'^register', CreateUserView.as_view(), name='register_user'),
    re_path(r'^agmcontributions', AGMCreateView.as_view(), name='AGM_contributions'),
    re_path(r'^agmbalances', AGMBalancesView.as_view(), name='AGM_balances'),
    re_path(r'^members', membersView.as_view(), name='members'),
]