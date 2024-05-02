from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate



# Create your views here.

def index(request):
    return render(request, 'palavrao/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return index(request)
        else:
            return render(request, 'palavrao/errologin.html')
    else:
        return render(request, 'palavrao/login.html')

def errologin(request):
    render(request, 'palavrao/errologin.html')
