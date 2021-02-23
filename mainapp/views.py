from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Главная страница
    """    
    template_name = 'mainapp/index.html'
    extra_context = {'title_name': 'GeekStaff'}


def login(request):
    return render(request, 'mainapp/user-login.html')
    

def register(request):
    return render(request, 'mainapp/user-register.html')
    

def forget_pass(request):
    return render(request, 'mainapp/user-forget-pass.html')