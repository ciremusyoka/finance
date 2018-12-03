from django.db import models
from django.contrib.auth.models import AbstractUser


# auto date and time generator abstract
class DateTimeAbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

#         user model
class MyUser(AbstractUser):
    SEX=(('MALE','Male'),('FEMALE','Female'))
    dob=models.DateField('date of birth',null=True, blank=True)
    image=models.ImageField(null=True,blank=True)
    gender=models.CharField(max_length=5,choices=SEX)
    sir_name =models.CharField(max_length=50,null=True, blank=True)


    def __str__(self):
        return self.first_name

class members(DateTimeAbstractModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)


    class Meta:
        verbose_name_plural = "Members"

    def __str__(self):
        return str(self.id)

#   user AGM contribution model
class AGMContributions(DateTimeAbstractModel):
    amount_paid = models.DecimalField(decimal_places=2, max_digits=1000000)
    owner = models.ForeignKey(MyUser, related_name='user_AGM', on_delete=models.CASCADE)
    year = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = "AGM  payments"

    def __str__(self):
        return str(self.id)


#   user AGM balances model
class AGMBalances(DateTimeAbstractModel):
    balance = models.DecimalField(decimal_places=2, max_digits=1000000)
    owner = models.ForeignKey(MyUser, related_name='user_AGM_balances', on_delete=models.CASCADE)
    year = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = "AGM balances"

    def __str__(self):
        return str(self.id)