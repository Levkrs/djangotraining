from django.shortcuts import render


def login(request):
    return render(request, 'authapp/user-login.html')


def register(request):
    return render(request, 'authapp/user-register.html')


def forget_pass(request):
    return render(request, 'authapp/user-forget-pass.html')
