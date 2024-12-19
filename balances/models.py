from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Bank(models.Model):
    name = models.CharField(max_length=150)
    acc_number = models.CharField(max_length= 200 , null=True)

    def __str__(self):
        return self.name
    
class Deposit(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    bank = models.CharField(max_length=150)
    account = models.CharField(max_length=200)
    amount = models.IntegerField()
    slip = models.ImageField(upload_to= "Deposit_slips" , null=True , blank=True)
    is_approved = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)

class Withdraw(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    bank = models.CharField(max_length=150)
    account = models.CharField(max_length=200)
    amount = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)