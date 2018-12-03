from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import payments, interests
from appmanager.models import AGMContributions, AGMBalances


# signal to create interests of balances when a payment is made
@receiver(post_save, sender=payments)
def add_interest(instance, created,**kwargs):
    if created:
        bal = instance.interest
        interests.objects.create(interest_accrued=bal, loan=instance.loan, owner=instance.owner)


# signal to update balance when AGM contribution is made
@receiver(post_save, sender=AGMContributions)
def update_balance(instance, created, **kwargs):
    if instance.overdue > 0:
        year = int(instance.year)+1
        AGMBalances.objects.create(balance=instance.overdue, year=str(year), owner=instance.owner)
    if instance.payments == 0:
        AGMBalances.objects.create(balance=instance.balance, year=instance.year, owner=instance.owner)
    else:
        AGMBalances.objects.filter(owner=instance.owner, year=instance.year).update(balance=instance.balance)