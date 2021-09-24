from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Accounts(request):
    return HttpResponse("Here is site's account")
