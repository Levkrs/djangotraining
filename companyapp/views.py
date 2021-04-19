"""
Views of company
"""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView
from django.views.generic.edit import FormMixin

from authapp.models import MyUser
from mainapp.models import FullInvite
from .models import Company, Job, FavoritesVacancies
from applicantapp.models import Resume, FavoritesResume
from authapp.permissions import CompanyPermissionMixin
from .forms import ResumeSearchForm, CompanyUpdateForm


# from icecream import ic


class ProfileView(LoginRequiredMixin, ListView):
    """ ЛК Компании """
    template_name = 'companyapp/profile.html'


    def get_queryset(self):
        """Выводим список вакансий компании"""
        return Job.objects.filter(company__user=self.request.user)


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
    form_class = CompanyUpdateForm
    template_name = 'companyapp/company_form.html'

    def get_success_url(self):
        return reverse_lazy('companyapp:profile', args=(self.request.user.id,))


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
        return reverse_lazy('companyapp:profile', args=(self.request.user.id,))


class JobDetailView(LoginRequiredMixin, CompanyPermissionMixin, DetailView):
    model = Job
    fields = ('status', 'grade', 'category', 'salary', 'city', 'employment', 'skills',
              'work_schedule', 'experience', 'short_description', 'description',)

    template_name = 'companyapp/job_detail.html'



class JobListView(LoginRequiredMixin, ListView):
    """
    Список вакансий пользователя
    """
    model = Job
    fields = '__all__'

    def get_queryset(self):
        return Job.objects.filter(company__user=self.request.user).exclude(status=9)


class ResumeListHR(LoginRequiredMixin, ListView):
    """
    Список резюме c пагинацие по 25 штук
    """
    model = Resume
    paginate_by = 25
    template_name = 'companyapp/resume_list_hr.html'

    def get_queryset(self):
        print('sda')
        cmp = Job.objects.filter(status=3, company=self.request.user.company).count()

        if Job.objects.filter(status=3, company=self.request.user.company).count() > 0 :
            return Resume.objects.filter(status='3')
        else:
            return []
    
    
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

class ResumeSearchList(ListView, FormMixin):
    """Поиск резюме"""
    model = Resume
    template_name = 'companyapp/resume_search.html'
    paginate_by = 10
    form_class = ResumeSearchForm


    def get_queryset(self):
        search_field = self.request.GET.get('search_field', None)
        city_field = self.request.GET.get('city_field', None)
        education_type = self.request.GET.get('education_type', None)
        employment = self.request.GET.get('employment', None)
        work_schedule = self.request.GET.get('work_schedule', None)

        query_params = {
            'search_field': search_field, 'city': city_field, 'education_type': education_type,
            'employment': employment, 'work_schedule': work_schedule
        }


        QUERY = []

        for field_name, field in query_params.items():
            if field_name == 'search_field' and field:
                QUERY.append((Q(headline__icontains=field) | Q(key_skills__icontains=field)))
            elif field_name == 'city' and field:
                QUERY.append(Q(city__icontains=field))
            elif field and field != '':
                QUERY.append(Q(**{field_name: field}))


        if any(QUERY):
            object_list = Resume.objects.filter(*QUERY)
            return object_list

        return Resume.objects.filter(status='3')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_count']= Job.objects.filter(company= self.request.user.company.id, status=3).count()
        # context['resume_count'] = Resume.objects.filter(user=self.request.user.id, status=3).count()
        print(context)
        return context

class ResponceRec(ListView):

    """
    Запросы на собеседование от REC
    """
    model = FullInvite
    template_name = 'companyapp/responce_rec.html'


    def get_queryset(self):
        job_list_id = list(Job.objects.filter(company_id=self.request.user.company.id).values_list('id', flat=True))
        object_list = FullInvite.objects.filter(vacansy_id__in=job_list_id).filter(aprove_hr=False)

        return object_list


class RespJobDetail(LoginRequiredMixin, DetailView):
    """
    Развернуть резюме подробнро
    """

    model = Resume

    template_name = 'companyapp/responce_rec_detail.html'

    def get_queryset(self):
        req = Resume.objects.filter(id=self.kwargs['pk'])
        print(req)
        return req

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddDeleteVacancyToFavorites(LoginRequiredMixin, View):
    """
    Добавление / удаление вакансии в/из избранное
    """

    def get(self, request, pk):
        job = Job.objects.get(id=pk)
        try:
            favorite = FavoritesVacancies.objects.create(user=request.user, job=job)
            favorite.save()
        except IntegrityError:
            favorite = FavoritesVacancies.objects.get(user=request.user, job=job)
            favorite.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class FavoriteResumeList(LoginRequiredMixin, ListView):
    """
    Список избранного пользователя
    """
    template_name = 'companyapp/favorite_resume_list.html'

    def get_queryset(self):
        favorite_resume = FavoritesResume.objects.filter(user=self.request.user.id).values('resume')
        resume_ids = [x['resume'] for x in favorite_resume]
        return Resume.objects.filter(pk__in=resume_ids).exclude(status=9)