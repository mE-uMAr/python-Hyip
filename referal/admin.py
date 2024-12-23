from django.contrib import admin
from .models import *

@admin.register(Referal)
class ReferalAdmin(admin.ModelAdmin):
    list_display = ('user' , 'code' , 'ref_by')
@admin.register(SetRefReward)
class SetRefRewardAdmin(admin.ModelAdmin):
    list_display = ('refReward' , 'maxRefs')
