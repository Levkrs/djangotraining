from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from companyapp.models import Job


class Index(TemplateView):
    """
    Главная страница
    """    
    template_name = 'mainapp/index.html'
    extra_context = {'title_name': 'GeekStaff'}

