from django.contrib import admin
from .models import *

@admin.register(Vip)
class VipAdmin(admin.ModelAdmin):
    list_display = ('vipName' , 'price' , 'daily')
@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user' , 'amount')
@admin.register(Invest)
class InvestAdmin(admin.ModelAdmin):
    list_display = ('user' , 'vipName' , 'income' , 'is_active')