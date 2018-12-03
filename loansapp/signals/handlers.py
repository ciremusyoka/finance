from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import payments, loans, interests
from pledgesapp.models import PledgePayments, AllPledges


# a signal to update balances when payments are made
@receiver(post_save, sender=payments)
def update_loan_balance(instance, created, **kwargs):
    instance.loan.balance = instance.balance
    instance.loan.save()


# a signal to create interests when a loan is taken
@receiver(post_save, sender=loans)
def create_interest(instance, created, **kwargs):
    if created:
        amount = instance.amount
        interest = amount*0.1
        interests.objects.create(interest_accrued=interest, loan=instance, owner=instance.owner)


# a signal to update pledge balance when payment is made
@receiver(post_save, sender=PledgePayments)
def update_pledge_balance(created, instance, **kwargs):
    if hasattr(instance, 'balance'):
        instance.pledge.balance = instance.balance
        instance.pledge.save()


# a signal to create payment when they are made together with pledges
@receiver(post_save, sender=AllPledges)
def create_pledge_payment(created, instance, **kwargs):
    if instance.initial_payment is not None or '':
        PledgePayments.objects.create(pledge=instance, amount_paid=instance.initial_payment)
