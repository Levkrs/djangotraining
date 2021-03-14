from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy

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

    def get(self, request, *args, **kwargs):
        Company.views_counter(kwargs['pk'])
        return super().get(self, request, *args, **kwargs)


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """
    Редактор карточки компании
    """
    model = Company
    fields = ('name', 'logo', 'headline', 'short_description', 'detail', 'location', 'link',)

    def get_success_url(self):
        return reverse_lazy('companyapp:card', args=[self.object.pk])
