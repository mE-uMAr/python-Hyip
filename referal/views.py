from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from invest import models
User = get_user_model
from .utils import ref_count,referances

@login_required
def invite(request):
    user = request.user

    ref_code = Referal.objects.get(user=user).code
    host = request.get_host()
    refs = ref_count(user)

    check_ref_reward = SetRefReward.objects.all()[0]
    max_ref = check_ref_reward.maxRefs
    ref_reward = check_ref_reward.refReward
    total_reward = refs * ref_reward

    created = False

    if request.method == 'POST':
        reward_add, created = Reward_add.objects.get_or_create(user=user)

        if created or (reward_add.total_refs < refs):
            new_refs = refs - reward_add.received
            up_balance = new_refs * ref_reward

            balance, creat = models.Balance.objects.get_or_create(user=user, defaults={'amount': 0})
            user_balance = balance.amount
            user_balance += up_balance
            if reward_add.total_refs <= max_ref:
                balance.amount = user_balance
                balance.save()
           

            reward_add.new_refs = new_refs
            reward_add.received = refs
            reward_add.total_refs = refs
            reward_add.save()
            messages.success(request, f'Rewards updated! ')
        else:
            messages.info(request, 'No new referrals try inviting users to get reward')

    param = {
        'code': ref_code,
        'host': host,
        'refs': refs,
        'ref_reward': ref_reward,
        'max_ref': max_ref,
        'total_reward': total_reward,
    }
    return render(request, 'invite.html', param)
