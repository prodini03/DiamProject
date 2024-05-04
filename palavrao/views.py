from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate

from palavrao.models import Client


# Create your views here.

def index(request):
    return render(request, 'palavrao/index.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return index(request)
        else:
            return render(request, 'palavrao/errologin.html',{'error_message': 'Enganaste-te no username ou na password'})
    else:
        return render(request, 'palavrao/login.html')

def errologin(request):
    render(request, 'palavrao/errologin.html')


def criarconta(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            client = Client(user=user)
            client.save()
            login(request, user)
            return redirect('palavrao:index')
        else:
            return render(request, 'palavrao/errologin.html', {'error_message': 'Username já existe'})
    else:
        return render(request, 'palavrao/criarconta.html')
