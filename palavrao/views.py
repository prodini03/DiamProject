import os

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate

from palavrao.models import Client

def index(request):
    imagem = existe_imagem_perfil(request.user.id)
    verificar = verificar_login(request)
    return render(request, 'palavrao/index.html',{'imagem':imagem,'verificar':verificar})

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

def fazer_upload(request):
    imagem = existe_imagem_perfil(request.user.id)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(str(request.user.id)+".jpg", myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'palavrao/fazer_upload.html', {'uploaded_file_url': uploaded_file_url, "imagem": imagem})
    return render(request,'palavrao/fazer_upload.html', {"imagem": imagem})


def existe_imagem_perfil(user_id):
    fs = FileSystemStorage()
    caminho_imagem = fs.path(os.path.join(f'{str(user_id)}.jpg'))
    print(caminho_imagem)
    return os.path.exists(caminho_imagem)

def dados_pessoais(request):
    user = request.user
    client = user.client
    imagem = existe_imagem_perfil(request.user.id)
    context = {
        'user': user,
        'client': client,
        'imagem': imagem
    }
    return render(request, 'palavrao/dados_pessoais.html', context)


def verificar_login(request):
    if request.user.is_authenticated:
        # O usuário está logado
        return True
    else:
        # O usuário não está logado, redirecione para a página de login
        return False

def logoutview(request):
    logout(request)
    return render(request, 'palavrao/logoutview.html')