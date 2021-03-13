from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, UpdateView

from .models import Company, Job


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    ЛК Компании
    """    
    template_name = 'companyapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyDetailView(LoginRequiredMixin, DetailView):
    """
    Карточка компании
    """
    model = Company


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """
    Редактор карточки компании
    """
    model = Company
    fields = '__all__'
