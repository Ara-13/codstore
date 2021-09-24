from django.urls import path, include
from . import views

app_name = 'buyaccount'

urlpatterns = [
    path('', views.Accounts, name='BuyAccount')
]
