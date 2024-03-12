#from django.contrib import admin

from django.urls import path
from app import views

urlpatterns = [
    # rota -> view responsável -> nome de referência
    #pagina inicial da usuarios.com
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
