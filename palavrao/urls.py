from django.urls import include, path
from . import views

app_name = 'palavrao'

urlpatterns = [
    path("", views.login, name='login'),
    path("index", views.index, name='index'),
    path('errologin',views.errologin, name='errologin'),
]
