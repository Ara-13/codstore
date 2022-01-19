from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from time import sleep

app_name="Sell"

def index(request, ):
    accounts_list = models.Account.objects.order_by('-code')
    accounts_list2 = models.Account.objects.order_by('-w_code')
    context = {
        'accounts_list': accounts_list,
        'accounts_list2': accounts_list2,
    }

    return render(request, 'Sell/accounts_list.html', context)

def account_view(request, co):
    account_detail = get_object_or_404(models.Account, pk=co)
    p_names = []

    for p in account_detail.accountpictures_set.all():
        split_list = str(p.picture).split('/')
        p_names.append(split_list.pop())

    context = {
        'account' : account_detail,
        'account_picture' : account_detail.accountpictures_set.all(),
        'picturenames' : p_names,
     }
    
    return render(request, 'Sell/accounts_info.html', context)

def account_p_view(request, wco):
    account = models.Account.objects.filter(p_status__exact='w')
    account_detail = get_object_or_404(account, w_code=wco)
    context = {
        'account' : account_detail,
        'account_picture' : account_detail.accountpictures_set.all()
     }
    return render(request, 'Sell/accounts_info.html', context)

@login_required(login_url='/login')
def account_form(request, ):
    code = models.Account.objects.all().count()+1
    main_code = models.Account.objects.filter(p_status__exact='w').count()+1
    level = request.POST.get('level')
    region = request.POST.get('region')
    rank = request.POST.get('rank')
    battle_pass = request.POST.get('battle_pass')
    description = request.POST.get('description')
    price = request.POST.get('price')

    if level or price:
        account = models.Account(code=code, w_code= main_code, level= level, region=region,
                                 rank=rank, description=description, price=price, battle_pass=battle_pass,
                                 p_status='w')
        account.save()

    return render(request, 'Sell/account_form.html', {'code' : main_code, 'name' : region})

def LoginFunc(request):
    message = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try: 
            user = User.objects.get(username=username)
        except:
            message = "Something is Wrong!"
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            message = "You Successfully logged in!"
            return redirect('sellaccount:list_view')
        else:
            message = "Something is Wrong! Check the Username And Password"

    final_message = message if message != None else ''
    context = {
        'message' : final_message,
    }
    return render(request, 'Sell/login.html', context)

def LogoutFunc(request):
    logout(request)
    return redirect('sellaccount:list_view')