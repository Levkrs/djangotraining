from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Company, Job


class ProfileView(LoginRequiredMixin, TemplateView):
    """ ЛК Компании """    
    template_name = 'companyapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyDetailView(LoginRequiredMixin, DetailView):
    """ Карточка компании """
    model = Company

    def get(self, request, *args, **kwargs):
        """ Счётчик просмотров """
        Company.views_counter(self.kwargs['pk'])
        return super().get(self, request, *args, **kwargs)
        # TODO  исключить из счета владельца, чтобы избежать накрутки


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактор карточки компании """
    model = Company
    fields = ('name', 'logo', 'headline', 'short_description', 'detail', 'location', 'link',)

    def get_success_url(self):
        return reverse_lazy('companyapp:card', args=[self.object.pk])


class JobCreateView(LoginRequiredMixin, CreateView):
    """ Карточка вакансии (создание) """
    model = Job
    fields = ('status', 'grade', 'category', 'salary', 'city', 'employment', 'skills',
              'work_schedule', 'experience', 'short_description', 'description',)

    def form_valid(self, form):
        form.instance.company_id = self.request.user.company
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактор карточки вакансии """
    model = Job
    fields = ('status', 'grade', 'category', 'salary', 'city', 'employment', 'skills',
              'work_schedule', 'experience', 'short_description', 'description',)
