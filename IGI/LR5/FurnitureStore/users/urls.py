from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^register/$', views.register, name='client_register'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^employee/register/$', views.employee_register, name='employee_register'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^logout/$', views.logout, name='logout')
]