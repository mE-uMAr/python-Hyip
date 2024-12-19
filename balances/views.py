from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from invest.models import *

User = get_user_model()

@login_required
def deposit(request):
    if request.method == 'POST':
        bank_id = request.POST.get('select')
        account = request.POST.get('account')
        amount = request.POST.get('amount')
        try:
            if bank_id and account and amount:
                deposit = Deposit.objects.create(
                    user = request.user,
                    bank = bank_id,
                    account = account,
                    amount = int(amount) ,
                )
            
                return redirect(reverse('pay', args=[deposit.id]))

        except Exception as e:
            print(f"Error occurred: {e}")

    bank2 = Bank.objects.all()
    param = {'bank2' : bank2}
    return render(request , 'deposit.html' , param)

@login_required
def pay(request , deposit_id):
    deposit = get_object_or_404(Deposit, id=deposit_id, user=request.user)

    if request.method == "POST":
        slip = request.FILES.get("slip")
        if slip:
            deposit.slip = slip
            deposit.save()
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
      <p class="message">Deposit submitted please wait .......</p>
      <a href="/" class="home-button">Home</a>
    </div>''')
        else:
            return HttpResponse("Please upload a valid file.")
        
    bank = deposit.bank
    amount = deposit.amount
    account = Bank.objects.filter(name = bank)
    param = {'amount' : amount , 'account' : account}
    return render(request , 'pay.html' ,param)

@login_required
def withdraw(request):
    user = request.user
    balance = Balance.objects.get(user = user)
    if request.method == 'POST':
        bank_id = request.POST.get('select')
        account = request.POST.get('account')
        amount = request.POST.get('amount')
        
        try:
            if bank_id and account and amount and int(amount)<=balance.amount:
                Withdraw.objects.create(
                    user = request.user,
                    bank = bank_id,
                    account = account,
                    amount = int(amount) ,
                )
            
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
      <p class="message">Withdraw submitted please wait .......</p>
      <a href="/" class="home-button">Home</a>
    </div>''')
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
      <p class="message">Information is not Authentic or insufficient balance....</p>
      <a href="/" class="home-button">Home</a>
    </div></body>''')

        except Exception as e:
            print(f"Error occurred: {e}")

    bank2 = Bank.objects.all()
    param = {'bank2' : bank2 , 'balance' : balance}
    return render(request , 'withdraw.html' , param)
