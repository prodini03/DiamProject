from django.urls import include, path
from . import views
from .views import LoginView

app_name = 'palavrao'

urlpatterns = [
    path("", views.loginview, name='login'),
    path("index", views.index, name='index'),
    path('errologin',views.errologin, name='errologin'),
    path('criarconta', views.criarconta, name='criarconta'),
    path('dados_pessoais', views.dados_pessoais, name='dados_pessoais'),
    path('fazer_upload', views.fazer_upload, name='fazer_upload'),
    path('logoutview', views.logoutview, name='logoutview'),
    path('comentarios', views.comentarios, name='comentarios'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('detalhe/<int:comentario_id>', views.detalhe, name='detalhe'),
    path('confirmardeletecomment/<int:comentario_id>', views.confirmardeletecomment, name='confirmardeletecomment'),
    path('apagarcomentario/<int:comentario_id>', views.apagarcomentario, name='apagarcomentario'),
    path('like_comment/<int:comentario_id>', views.like_comment, name='like_comment'),
    path('login/', LoginView.as_view()),
    path('api/comments/', views.comments),
]
