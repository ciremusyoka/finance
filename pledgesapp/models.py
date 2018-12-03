from django.db import models
from appmanager.models import DateTimeAbstractModel, members


#   the field for defining pledges
class PledgePurpose(DateTimeAbstractModel):
    purpose = models.CharField(max_length=200)
    beneficiary = models.CharField(max_length=200)
    deadline = models.DateField(blank=True, null=True)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=1000000, blank=True, null=True)

    def __str__(self):
        return self.purpose


#   pledges fields
class AllPledges(DateTimeAbstractModel):
    purpose = models.ForeignKey(PledgePurpose, related_name='all_pledges', on_delete=models.CASCADE)
    member = models.ForeignKey(members, related_name='member', on_delete=models.CASCADE)
    pledge_amount = models.DecimalField(decimal_places=2, max_digits=1000000)
    balance = models.DecimalField(decimal_places=2, max_digits=1000000, blank=True, null=True)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=1000000, blank=True, null=True)
    initial_payment = models.DecimalField(decimal_places=2, max_digits=1000000, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "pledges"


#   pledges payment model
class PledgePayments(DateTimeAbstractModel):
    pledge = models.ForeignKey(AllPledges, related_name='pledge_payments', on_delete=models.CASCADE)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=1000000)

    class Meta:
        verbose_name_plural = "Pledge payments"