from django.contrib import admin
from .models import loans, payments, interests

class loansadmin(admin.ModelAdmin):
    list_display = ['owner', 'amount', 'balance', 'created', 'id']

admin.site.register(loans, loansadmin)

class paymentsadmin(admin.ModelAdmin):
    list_display = ['owner','loan', 'amount_paid', 'balance', 'created', 'id']

admin.site.register(payments, paymentsadmin)

class interestsadmin(admin.ModelAdmin):
    list_display = ['owner','loan', 'interest_accrued', 'created', 'id']

admin.site.register(interests, interestsadmin)
