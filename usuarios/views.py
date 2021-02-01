from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('o campo nome nao pode  ficar em branco')
            return redirect ('cadastro')
        if not email.strip():
            print('o campo email nao pode  ficar em branco')
            return redirect ('cadastro')
        if senha != senha2:
            print ('as senhas nao sao iguais')
            return redirect ('cadastro')
        if User.objects.filter(email=email).exists():
            print ('usuario ja existe')
            return redirect ('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('usuario cadastro')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('os campos email e senha nao podem ficar em branco')
            return redirect ('login')
        return redirect ('dashboard')
    return render(request,'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')