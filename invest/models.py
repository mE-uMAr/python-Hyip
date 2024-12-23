from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Vip(models.Model):
    vipName = models.CharField(max_length=100)
    price = models.IntegerField()
    daily = models.IntegerField()
    vip_image = models.ImageField(upload_to='vip')

class Balance(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    amount = models.IntegerField(default=10)

class Invest(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    vipName = models.CharField(max_length=300)
    income = models.IntegerField()
    price = models.IntegerField()
    is_active = models.BooleanField(default = True)