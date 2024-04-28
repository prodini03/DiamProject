from django.urls import include, path
from . import views

app_name = 'palavrao'

path('login',views.login,name='login')

