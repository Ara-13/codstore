from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

app_name="Sell"

def index(request, ):
    accounts_list = models.Account.objects.all()
    context = {
        'accounts_list': accounts_list,
    }
    return render(request, 'Sell/index.html', context)
