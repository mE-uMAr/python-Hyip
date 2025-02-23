from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from invest.models import *
import random

User = get_user_model()

@login_required
def deposit(request):
    if request.method == 'POST':
        bank_id = request.POST.get('select')
        account = request.POST.get('account')
        amount = request.POST.get('amount')
        try:
            if bank_id and account and amount:
                if int(amount) < 500:
                    return redirect("/balance/deposit/")
                else:
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
    qr = Qrs.objects.all()
    if request.method == "POST":
        slip = request.FILES.get("slip")
        if slip:
            deposit.slip = slip
            deposit.save()
            return HttpResponse('''<!DOCTYPE html>
         <html lang="en">
         <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Deposit Confirmation</title>
         <style>
        :root {
            --background-color: #306998;
            --container-background: #fff;
            --text-color: #000000;
            --button-color: #0066cc;
            --button-hover: #0052a3;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--background-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            color: var(--text-color);
        }

        .container {
            background-color: var(--container-background);
            padding: 40px;
            border-radius: 15px;
            width: 100%;
            max-width: 400px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            animation: fadeIn 0.5s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .message {
            font-size: 20px;
            margin-bottom: 30px;
            line-height: 1.4;
        }

        .loading-dots {
            display: inline-block;
        }

        .loading-dots::after {
            content: '...';
            animation: loading 1.5s steps(4, end) infinite;
        }

        @keyframes loading {
            0%, 100% { content: ''; }
            25% { content: '.'; }
            50% { content: '..'; }
            75% { content: '...'; }
        }

        .home-button {
            background-color: var(--button-color);
            color: var(--text-color);
            border: none;
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            font-weight: 600;
        }

        .home-button:hover {
            background-color: var(--button-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 102, 204, 0.3);
        }

        .home-button:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.5);
        }

        @media (max-width: 480px) {
            .container {
                padding: 30px 20px;
            }

            .message {
                font-size: 18px;
            }

            .home-button {
                padding: 10px 24px;
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <p class="message">Deposit submitted, please wait<span class="loading-dots"></span></p>
        <a href="/" class="home-button">Return Home</a>
    </div>
</body>
</html>

''')
        else:
            return HttpResponse("Please upload a valid file.")
    img = random.choice(qr)
    bank = deposit.bank
    amount = deposit.amount
    account = Bank.objects.filter(name = bank)
    param = {'amount' : amount , 'account' : account , 'img':img}
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

                return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deposit Confirmation</title>
    <style>
        :root {
            --background-color: #306998;
            --container-background: #ffffff;
            --text-color: #000000;
            --button-color: #0066cc;
            --button-hover: #0052a3;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--background-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            color: var(--text-color);
        }

        .container {
            background-color: var(--container-background);
            padding: 40px;
            border-radius: 15px;
            width: 100%;
            max-width: 400px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            animation: fadeIn 0.5s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .message {
            font-size: 20px;
            margin-bottom: 30px;
            line-height: 1.4;
        }

        .loading-dots {
            display: inline-block;
        }

        .loading-dots::after {
            content: '...';
            animation: loading 1.5s steps(4, end) infinite;
        }

        @keyframes loading {
            0%, 100% { content: ''; }
            25% { content: '.'; }
            50% { content: '..'; }
            75% { content: '...'; }
        }

        .home-button {
            background-color: var(--button-color);
            color: var(--text-color);
            border: none;
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            font-weight: 600;
        }

        .home-button:hover {
            background-color: var(--button-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 102, 204, 0.3);
        }

        .home-button:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.5);
        }

        @media (max-width: 480px) {
            .container {
                padding: 30px 20px;
            }

            .message {
                font-size: 18px;
            }

            .home-button {
                padding: 10px 24px;
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <p class="message"> Withdraw submitted, please wait<span class="loading-dots"></span></p>
        <a href="/" class="home-button">Return Home</a>
    </div>
</body>
</html>

''')
            else:
                return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deposit Confirmation</title>
    <style>
        :root {
            --background-color: ##306998;
            --container-background: #ffffff;
            --text-color: #000000;
            --button-color: #0066cc;
            --button-hover: #0052a3;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--background-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            color: var(--text-color);
        }

        .container {
            background-color: var(--container-background);
            padding: 40px;
            border-radius: 15px;
            width: 100%;
            max-width: 400px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            animation: fadeIn 0.5s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .message {
            font-size: 20px;
            margin-bottom: 30px;
            line-height: 1.4;
        }

        .loading-dots {
            display: inline-block;
        }

        .loading-dots::after {
            content: '...';
            animation: loading 1.5s steps(4, end) infinite;
        }

        @keyframes loading {
            0%, 100% { content: ''; }
            25% { content: '.'; }
            50% { content: '..'; }
            75% { content: '...'; }
        }

        .home-button {
            background-color: var(--button-color);
            color: var(--text-color);
            border: none;
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            font-weight: 600;
        }

        .home-button:hover {
            background-color: var(--button-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 102, 204, 0.3);
        }

        .home-button:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.5);
        }

        @media (max-width: 480px) {
            .container {
                padding: 30px 20px;
            }

            .message {
                font-size: 18px;
            }

            .home-button {
                padding: 10px 24px;
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <p class="message"> Unauthentic imformation of insufficient ballance !</p>
        <a href="/" class="home-button">Return Home</a>
    </div>
</body>
</html>

''')

        except Exception as e:
            print(f"Error occurred: {e}")

    bank2 = Bank.objects.all()
    param = {'bank2' : bank2 , 'balance' : balance}
    return render(request , 'withdraw.html' , param)
