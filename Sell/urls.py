from django.urls import re_path, include
from . import views

app_name= 'sellaccount'

urlpatterns = [
    re_path(r'^$', views.index, name='list_view'),
    re_path(r'^(?P<co>[0-9]{1})$', views.account_view, name='detail_view'),
    re_path(r'^0(?P<wco>[0-9]{1})$', views.account_p_view, name='p_detail_view'),
    re_path(r'^form$', views.account_form),
    re_path(r'^login$', views.LoginFunc, name="Login"),
    re_path(r'^logout$', views.LogoutFunc, name="Logout"),
]
