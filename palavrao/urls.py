from django.urls import include, path
from . import views

app_name = 'palavrao'

urlpatterns = [
    path('login', views.login, name='login'),
    path("", views.index, name='index'),
    path('errologin',views.errologin, name='errologin'),
]
