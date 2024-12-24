from django.shortcuts import render ,redirect , HttpResponseRedirect , HttpResponse
from .models import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from balances.models import *
from django.contrib.auth import get_user_model
from referal.models import *
User = get_user_model()

@login_required
def home(request):
    user = request.user
    try:
        balance = Balance.objects.get(user=user)
    except Balance.DoesNotExist:
        balance = Balance.objects.create(user = user , amount = 0)

    user_balance = balance.amount
    if request.method == 'POST':
        vip_name = request.POST.get('vip')
        income = request.POST.get('income')
        price = request.POST.get('price')
        if int(price)<=user_balance:
            invest = Invest.objects.create(
                user = user ,
                vipName = vip_name ,
                income = income ,
                price = price
            )
            balance.amount -= int(price)
            balance.save()
            return HttpResponseRedirect('/invest/')
        else:
            return HttpResponse('''<style>
      body {
        font-family: Arial, sans-serif;
        background-color: #000000;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        padding: 20px;
        box-sizing: border-box;
        color: white;
      }
      .container {
        background-color: #1c1c1c;
        padding: 30px;
        border-radius: 10px;
        width: 100%;
        max-width: 400px;
        text-align: center;
      }
      .message {
        font-size: 18px;
        margin-bottom: 20px;
      }
      .home-button {
        background-color: #0066cc;
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        text-decoration: none;
        display: inline-block;
      }
      .home-button:hover {
        background-color: #0052a3;
      }
      .home-button:focus {
        outline: none;
        box-shadow: 0 0 0 2px #0066cc;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <p class="message">insufficient balance....</p>
      <a href="/balance/deposit/" class="home-button">Recharge Now</a>
    </div></body>''')
    vip_all = Vip.objects.all()
    calc_hourly=[] 
    for vip in vip_all:
        hourly = vip.daily/24
        calc_hourly.append({'vip' : vip , 'hourly' : hourly})

    param = {'calc' : calc_hourly}
    return render(request , 'home.html' , param)
def login_user(request):
    if request.method == 'POST':
        p_number = request.POST['phone']
        password = request.POST['password']
        if not User.objects.filter(p_number = p_number).exists():
            messages.error(request , "User dosn't exist")
            return redirect('/signup/') 
        user = authenticate(p_number = p_number , password = password)
        if user is None:
            messages.error(request , 'Password is incorrect !!')
            return redirect('/accounts/login/')
        else:
            login(request , user)
            return redirect('/')
    return render(request , 'login.html')

def signup_user(request , *args , **kwargs):
    if request.method == 'POST':
        p_number = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        code = request.POST.get('code')
        code_in = request.POST['code-in']
        profile_img = request.FILES.get('profile_image')
    
        if password1==password2:
            password = password1
        else:
            messages.error(request , "Mismatches try to resolve error first")
        
        user = User(p_number=p_number)
        user.set_password(password)
        if profile_img:
            user.profile_img = profile_img
        else: 
            None
            
        user.save()

        try:
            code = str(kwargs.get('ref_code'))
            ref = Referal.objects.get(code = code)
            ref_by = ref.user
            Referal.objects.create(user = user , ref_by = ref_by)
        except:
            Referal.objects.create(user = user)
            
        Reward_add.objects.create(user = user)
        
        messages.success(request , 'Account created successfully')
        return redirect('/') 
    return render(request , 'signup.html')


def logout_user(request):
    logout(request)
    return redirect('/accounts/login')
@login_required
def account(request):
    user = request.user
    balance = Balance.objects.filter(user = user)
    incoming = Deposit.objects.filter(user=user, is_approved=False, is_processed=True)
    outgoing = Withdraw.objects.filter(user=user, is_approved=False, is_processed=True)
    try:
        incoming_total = sum(int(item.amount) for item in incoming)
    except:
        incoming_total = 0
    try:
        outgoing_total = sum(int(item.amount) for item in outgoing)
    except:
        outgoing_total = 0
    param = {'user':user ,'balance' : balance , 'incoming' : incoming_total , 'incoming_transactions' : incoming , 'outgoing' : outgoing_total , 'outgoing_transactions' : outgoing}
    return render(request , 'account.html', param)
@login_required
def profile(request):
    user = request.user
    balance, created = Balance.objects.get_or_create(user=user, defaults={'amount': 0})
    user_balance = balance.amount
    deposits = Deposit.objects.filter(user=user, is_approved=True, is_processed=False)
    withdraws = Withdraw.objects.filter(user=user, is_approved=True, is_processed=False)

    for deposit in deposits:
        user_balance += int(deposit.amount) 
        deposit.is_approved = False
        deposit.is_processed = True  
        deposit.save()
    for withdraw in withdraws:
        user_balance -= int(withdraw.amount) 
        withdraw.is_approved = False
        withdraw.is_processed = True  
        withdraw.save()

    balance.amount = user_balance
    balance.save()

    dists = Cron.objects.all().count()

    param = {'user': user, 'balance': user_balance , 'dists' : dists}
    return render(request, 'profile.html', param)

def invest(request):
    user = request.user
    invests = Invest.objects.filter(user = user)
    return render(request , 'invest.html' , { 'invests': invests})
