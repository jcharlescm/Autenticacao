from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'auth/cadastro.html')
    # return render(request, 'auth/cadastro.html')


def login(request):
    return render(request, 'auth/login.html')
    # return render(request, 'auth/login.html')


