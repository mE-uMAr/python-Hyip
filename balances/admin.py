from django.contrib import admin
from .models import *

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user' , 'bank' , 'amount' , 'account' , 'is_approved' , 'is_processed')
@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('user' , 'bank' , 'amount' , 'account' , 'is_approved' , 'is_processed')
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name' , 'acc_number')

admin.site.register(Cron)