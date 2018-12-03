from django.contrib import admin
from .models import MyUser, AGMContributions, AGMBalances, members


class UsersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'sir_name', 'username', 'gender','id']
admin.site.register(MyUser, UsersAdmin)


class AGMContributionsAdmin(admin.ModelAdmin):
    list_display = ['owner', 'amount_paid', 'year', 'created', 'id']
admin.site.register(AGMContributions,AGMContributionsAdmin)


class AGMBalancesAdmin(admin.ModelAdmin):
    list_display = ['owner', 'balance', 'year', 'created', 'id']
admin.site.register(AGMBalances, AGMBalancesAdmin)


class membersAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','id']
admin.site.register(members, membersAdmin)