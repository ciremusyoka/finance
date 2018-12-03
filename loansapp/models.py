from django.db import models
from appmanager.models import DateTimeAbstractModel, MyUser

#   user loans model
class loans(DateTimeAbstractModel):
    amount = models.DecimalField(decimal_places=2, max_digits=1000000)
    balance = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=1000000)
    owner = models.ForeignKey(MyUser, related_name='user_loans', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "loans"

    def __str__(self):
        return str(self.id)


#   user loan payments model
class payments(DateTimeAbstractModel):
    amount_paid = models.DecimalField(decimal_places=2, max_digits=1000000)
    balance = models.DecimalField(decimal_places=2, null=True, blank=True , max_digits=1000000)
    loan = models.ForeignKey(loans, related_name='payments', on_delete=models.CASCADE)
    owner = models.ForeignKey(MyUser, related_name='user_payments', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Loan payments"

    def __str__(self):
        return str(self.id)


#   user loan interests model
class interests(DateTimeAbstractModel):
    interest_accrued = models.DecimalField(decimal_places=2, max_digits=1000000)
    loan = models.ForeignKey(loans, related_name='interests', on_delete=models.CASCADE)
    owner = models.ForeignKey(MyUser, related_name='user_interests', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "interests"

    def __str__(self):
        return str(self.id)
