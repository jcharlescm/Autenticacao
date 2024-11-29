from django.urls import path
from . import views  # Importe as views do app


urlpatterns = [
    path('auth/cadastro/', views.cadastro, name='cadastro'),  # Rota de cadastro
    path('auth/login/', views.login, name='login'),          # Rota de login
]