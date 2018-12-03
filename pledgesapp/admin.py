from django.contrib import admin
from .models import AllPledges, PledgePayments, PledgePurpose

class PledgePurposeAdmin(admin.ModelAdmin):
    list_display = ['purpose', 'beneficiary', 'deadline', 'created', 'amount_paid', 'id']
admin.site.register(PledgePurpose, PledgePurposeAdmin)


class PledgePaymentsAdmin(admin.ModelAdmin):
    list_display = ['pledge', 'amount_paid', 'id']
admin.site.register(PledgePayments, PledgePaymentsAdmin)


class AllPledgesAdmin(admin.ModelAdmin):
    list_display = ['purpose', 'member', 'pledge_amount', 'amount_paid', 'balance', 'created', 'id']
admin.site.register(AllPledges, AllPledgesAdmin)