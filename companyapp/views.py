from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView

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
