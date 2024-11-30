from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/auth/cadastro/
    path('cadastro/', views.cadastro, name='cadastro'),
    # http://127.0.0.1:8000/auth/login/
    path('login/', views.login, name='login'),
    # http://127.0.0.1:8000/auth/plataforma     --->> sem barra
    path('plataforma', views.plataforma, name='plataforma'),
]