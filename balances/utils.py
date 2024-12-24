from invest.models import Invest, Balance

def cron():
    invests = Invest.objects.all()
    for i in invests:
        user = i.user
        balance = Balance.objects.get(user = user)
        balance.amount += i.income
        balance.save()
        print(f"{balance.user}'s balance incremented with profit : {i.income}")