"""
Views of company
"""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .models import Company, Job
from applicantapp.models import Resume
from authapp.permissions import CompanyPermissionMixin
# from icecream import ic


class ProfileView(LoginRequiredMixin, ListView):
    """ ЛК Компании """
    template_name = 'companyapp/profile.html'


    def get_queryset(self):
        """Выводим список вакансий компании"""
        return Job.objects.filter(company__user_id=self.kwargs['pk'])

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


class CompanyUpdateView(LoginRequiredMixin, CompanyPermissionMixin, UpdateView):
    """ Редактор карточки компании """
    model = Company
    fields = ('name', 'logo', 'headline', 'short_description', 'detail', 'location', 'link',)

    def get_success_url(self):
        return reverse_lazy('companyapp:card', args=[self.object.pk])


class JobCreateView(LoginRequiredMixin, CompanyPermissionMixin, CreateView):
    """ Карточка вакансии (создание) """
    model = Job
    fields = ('status', 'grade', 'category', 'salary', 'city', 'employment', 'skills',
              'work_schedule', 'experience', 'short_description', 'description',)


    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, CompanyPermissionMixin, UpdateView):
    """ Редактор карточки вакансии """
    model = Job
    fields = ('status', 'grade', 'category', 'salary', 'city', 'employment', 'skills',
              'work_schedule', 'experience', 'short_description', 'description',)
    template_name = 'companyapp/job_form_edit.html'

    def get_success_url(self):
        print(self.object.id)
        return reverse_lazy('companyapp:profile', args=(self.request.user.id,))



class JobListView(LoginRequiredMixin, ListView):
    """
    Список вакансий пользователя
    """
    model = Job
    fields = '__all__'

    def get_queryset(self):
        try:
            company = self.request.user.company
        except Exception:
            return self.model.objects.none()

        return company.jobs


class ResumeListHR(LoginRequiredMixin, ListView):
    """
    Список резюме c пагинацие по 25 штук
    """
    model = Resume
    paginate_by = 25
    template_name = 'companyapp/resume_list_hr.html'

    def get_queryset(self):
        return Resume.objects.filter(status='Опубликовано')
    
    
class ResumeListDetail(LoginRequiredMixin, DetailView):
    """
    Развернуть резюме подробнро
    """
    model = Resume
    template_name = 'companyapp/resume_detail.html'

    def get_queryset(self):
        req = Resume.objects.filter(pk=self.kwargs['pk'])
        return req

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ResumeSearchList(ListView):
    """Поиск резюме по краткому описанию"""
    model = Resume
    template_name = 'companyapp/resume_search.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Resume.objects.filter(
                Q(description__icontains=query) | Q(short_description__icontains=query)
            )
            return object_list
        else:
            return Resume.objects.all()