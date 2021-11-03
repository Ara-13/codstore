from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models
from django.http import HttpResponse

app_name="Sell"

def index(request, ):
    accounts_list = models.Account.objects.order_by('-code')
    context = {
        'accounts_list': accounts_list,
    }
    return render(request, 'Sell/accounts_list.html', context)

def account_view(request, co):
    account_detail = get_object_or_404(models.Account, pk=co)
    context = {
        'account' : account_detail,
        'account_picture' : account_detail.accountpictures_set.all()
     }
    return render(request, 'Sell/accounts_info.html', context)
