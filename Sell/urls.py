from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^(?P<co>[0-9]{1})$', views.account_view)
]
