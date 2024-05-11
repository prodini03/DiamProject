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
import random
from django.contrib.auth.decorators import login_required

from palavrao.models import Client, Comment, Likes
from django.http import JsonResponse


def index(request):
    imagem = existe_imagem_perfil(request.user.id)
    verificar = verificar_login(request)
    return render(request, 'palavrao/index.html', {'imagem': imagem, 'verificar': verificar})


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return index(request)
        else:
            return render(request, 'palavrao/errologin.html',
                          {'error_message': 'Enganaste-te no username ou na password'})
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


@login_required(login_url='/palavrao/loginview')
def fazer_upload(request):
    imagem = existe_imagem_perfil(request.user.id)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(str(request.user.id) + ".jpg", myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'palavrao/fazer_upload.html', {'uploaded_file_url': uploaded_file_url, "imagem": imagem})
    return render(request, 'palavrao/fazer_upload.html', {"imagem": imagem})


def existe_imagem_perfil(user_id):
    fs = FileSystemStorage()
    caminho_imagem = fs.path(os.path.join(f'{str(user_id)}.jpg'))
    print(caminho_imagem)
    return os.path.exists(caminho_imagem)


@login_required(login_url='/palavrao/loginview')
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


@login_required(login_url='/palavrao/loginview')
def add_comment(request):
    imagem = existe_imagem_perfil(request.user.id)
    if request.method == 'POST':
        text = request.POST.get('text')
        # Supondo que você já tenha o usuário autenticado
        user = request.user.client  # Obtém o cliente associado ao usuário
        comment = Comment.objects.create(user=user, text=text)
        comment.save()

        comments = Comment.objects.all()
        return comentarios(request)  # Redireciona para a página de comentários após adicionar o comentário
    return render(request, 'palavrao/add_comment.html',
                  {'imagem': imagem})  # Renderiza o formulário de adição de comentário se não for uma solicitação POST


@login_required(login_url='/palavrao/loginview')
def comentarios(request):
    comments = Comment.objects.all()
    imagem = existe_imagem_perfil(request.user.id)
    for comment in comments:
        comment.size = random.randint(15, 35)
    return render(request, 'palavrao/comentarios.html', {'comments': comments, 'imagem': imagem})


@login_required(login_url='/palavrao/loginview')
def detalhe(request, comentario_id):
    comment = get_object_or_404(Comment, pk=comentario_id)
    is_superuser = request.user.is_authenticated and request.user.is_superuser
    imagem = existe_imagem_perfil(request.user.id)
    return render(request, 'palavrao/detalhe.html',
                  {'comment': comment, 'is_superuser': is_superuser, 'imagem': imagem})


def check_superuser(user):
    return user.is_superuser


@user_passes_test(check_superuser, login_url='/palavrao/loginview')
def apagarcomentario(request, comentario_id):
    comment = get_object_or_404(Comment, pk=comentario_id)
    imagem = existe_imagem_perfil(request.user.id)
    return render(request, 'palavrao/apagarcomentario.html', {'comment': comment, 'imagem': imagem})


@user_passes_test(check_superuser, login_url='/palavrao/loginview')
def confirmardeletecomment(request, comentario_id):
    comment = get_object_or_404(Comment, pk=comentario_id)
    comment.delete()
    return comentarios(request)

def like_comment(request, comentario_id):
    comment = get_object_or_404(Comment, pk=comentario_id)
    user = request.user
    try:
        already_liked = Likes.objects.get(user=user, comment=comment)
        # User already liked the comment, so unlike it
        comment.gostos -= 1
        comment.save()
        already_liked.delete()
    except Likes.DoesNotExist:
        # User hasn't liked the comment yet, so like it
        comment.gostos += 1
        comment.save()
        Likes.objects.create(user=user, comment=comment)
    # Redirect back to the 'comentarios' URL using its name
    return redirect('palavrao:comentarios')