from django.db import models

# Create your models here.
tycr = (('Credit','Credit'),)
class CreditModel(models.Model):
    amt = models.PositiveBigIntegerField(default=0)
    tag = models.CharField(max_length=200,choices=tycr)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amt)

tyde = (('Debit','Debit'),)
class DebitModel(models.Model):
    amt = models.PositiveBigIntegerField(default=0)
    tag = models.CharField(max_length=200,choices=tyde)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amt)

ty = (('Credit Transfer','Credit Transfer'),('Debit Transfer','Debit Transfer'))
class BankTransferModel(models.Model):
    amt = models.PositiveBigIntegerField(default=0)
    tag = models.CharField(max_length=200,choices=ty)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amt)

btn = (('Credit','Credit'),('Debit','Debit'),('Credit Transfer','Credit Transfer'),('Debit Transfer','Debit Transfer'))
class CreditDebitTransferButtonModel(models.Model):
    amt = models.PositiveBigIntegerField(default=0)
    tag = models.CharField(max_length=200)
    btn_type = models.CharField(max_length=20,choices=btn)

    def __str__(self):
        return str(self.amt)