from django.urls import re_path
from .views import PledgePurposesView, CreatePledgeView
from .pledgepayments.views import PledgePaymentView

urlpatterns = [
    re_path(r'^allpledges', PledgePurposesView.as_view(), name='pledges'),
    re_path(r'^pledges', CreatePledgeView.as_view(), name='CreatePledgeView'),
    re_path(r'^paypledge', PledgePaymentView.as_view(), name='pledge_payments'),
]