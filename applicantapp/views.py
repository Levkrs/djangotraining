"""
Views of applicant
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView
from django.views.generic.edit import FormMixin
from django.forms import inlineformset_factory

from authapp.permissions import ApplicantPermissionMixin
from applicantapp.forms import ResumeUpdateForm, JobSearchForm, ResumeCreateForm
from applicantapp.models import Resume, FavoritesResume, Experience, Education
from companyapp.models import Job, FavoritesVacancies
from mainapp.models import FullInvite


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    ЛК Соискателя
    """
    template_name = 'applicantapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_list'] = Resume.objects.filter(user=self.request.user.pk)
        return context


class ResumeList(LoginRequiredMixin, ListView):
    """
    Список резюме пользователя
    """
    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user.id).exclude(status=9)


class CreateResume(LoginRequiredMixin, ApplicantPermissionMixin, CreateView):
    """
    Создание резюме
    """
    model = Resume
    template_name = 'applicantapp/create_resume.html'
    form_class = ResumeCreateForm

    def get_success_url(self):
        return reverse_lazy('applicantapp:profile', args=(self.request.user.id,))

    def dispatch(self, *args, **kwargs):
        return super(CreateResume, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super(CreateResume, self).get_context_data(**kwargs)
        EducationFormSet = inlineformset_factory(
            Resume, Education, form=ResumeCreateForm, extra=1)
        ExperienceFormSet = inlineformset_factory(
            Resume, Experience, form=ResumeCreateForm, extra=1)

        if self.request.POST:
            education_formset = EducationFormSet(self.request.POST)
            experience_formset = ExperienceFormSet(self.request.POST)
        else:
            education_formset = EducationFormSet()
            experience_formset = ExperienceFormSet()

        data['education'] = education_formset
        data['experience'] = experience_formset

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        education = context['education']
        experience = context['experience']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if education.is_valid():
                education.instance = self.object
                education.save()
            if experience.is_valid():
                experience.instance = self.object
                experience.save()

        return super(CreateResume, self).form_valid(form)


class UpdateResume(LoginRequiredMixin, ApplicantPermissionMixin, UpdateView):
    """
    Update Resume
    """
    model = Resume
    form_class = ResumeUpdateForm
    template_name = 'applicantapp/update_resume.html'

    def get_success_url(self):
        return reverse_lazy('applicantapp:profile', args=(self.request.user.id,))

    def get_context_data(self, **kwargs):
        data = super(UpdateResume, self).get_context_data(**kwargs)

        EducationFormSet = inlineformset_factory(
            Resume, Education, form=ResumeUpdateForm, extra=1)
        ExperienceFormSet = inlineformset_factory(
            Resume, Experience, form=ResumeUpdateForm, extra=1)

        if self.request.POST:
            data['education'] = EducationFormSet(self.request.POST, instance=self.object)
            data['experience'] = ExperienceFormSet(self.request.POST, instance=self.object)
        else:
            queryset_education = self.object.education.select_related()
            queryset_experience = self.object.experience.select_related()
            education_formset = EducationFormSet(
                instance=self.object, queryset=queryset_education)
            experience_formset = ExperienceFormSet(
                instance=self.object, queryset=queryset_experience)

            data['education'] = education_formset
            data['experience'] = experience_formset

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        education = context['education']
        experience = context['experience']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if education.is_valid():
                education.instance = self.object
                education.save()
            if experience.is_valid():
                experience.instance = self.object
                experience.save()

        return super(UpdateResume, self).form_valid(form)


class JobListDetail(LoginRequiredMixin, DetailView):
    """
    Развернуть вакансию подробнро
    """
    model = Resume
    template_name = 'applicantapp/job_detail.html'

    def get_queryset(self):
        req = Job.objects.filter(pk=self.kwargs['pk'])

        return req

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class JobSearchList(ListView, FormMixin):
    """Поиск вакансий"""
    model = Job
    template_name = 'applicantapp/job_search.html'
    paginate_by = 10
    form_class = JobSearchForm

    def get_queryset(self):

        search_field = self.request.GET.get('search_field', None)
        city_field = self.request.GET.get('city_field', None)
        # salary_field = self.request.GET.get('salary_field', None)
        choice_grade = self.request.GET.get('choice_grade', None)
        choice_category = self.request.GET.get('choice_category', None)
        choice_employment = self.request.GET.get('choice_employment', None)
        choice_work_shedule = self.request.GET.get('choice_work_shedule', None)
        choice_experience = self.request.GET.get('choice_experience', None)

        query_params = {
            'search_field': search_field, 'city': city_field, 'grade': choice_grade,
            'category': choice_category, 'employment': choice_employment,
            'work_schedule': choice_work_shedule, 'experience': choice_experience
        }

        QUERY = []

        for field_name, field in query_params.items():
            if field_name == 'search_field' and field:
                QUERY.append(
                    (Q(description__icontains=field) | Q(short_description__icontains=field)))
            elif field_name == 'city' and field:
                QUERY.append(Q(city__icontains=field))
            elif field and field != '':
                QUERY.append(Q(**{field_name: field}))

        if any(QUERY):
            object_list = Job.objects.filter(*QUERY)
            return object_list

        return Job.objects.filter(status='3')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_count'] = Resume.objects.filter(id=self.request.user.id, status=3).count()
        print(context)
        return context


class ResponceHr(ListView):
    """
    Приглащения от HR
    """

    model = FullInvite
    template_name = 'applicantapp/responce_hr.html'

    def get_queryset(self):
        resume_list_id = list(Resume.objects.filter(
            user=self.request.user.id).values_list('id', flat=True))
        object_list = FullInvite.objects.filter(
            recrut_resume_id__in=resume_list_id).filter(aprove_recrut=False)
        print('__')

        return object_list


class ResponceJobDetail(LoginRequiredMixin, DetailView):
    """
    Развернуть резюме подробнро
    """
    model = Job
    template_name = 'applicantapp/responce_job_detail.html'

    def get_queryset(self):
        req = Job.objects.filter(id=self.kwargs['pk'])
        return req

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddDeleteResumeToFavorites(LoginRequiredMixin, View):
    """
    Добавление / удаление вакансии в/из избранное
    """

    def get(self, request, pk):
        resume = Resume.objects.get(id=pk)
        try:
            favorite = FavoritesResume.objects.create(user=request.user, resume=resume)
            favorite.save()
        except IntegrityError:
            favorite = FavoritesResume.objects.get(user=request.user, resume=resume)
            favorite.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class FavoriteJobList(LoginRequiredMixin, ListView):
    """
    Список избранного пользователя
    """
    template_name = 'applicantapp/favorite_job_list.html'

    def get_queryset(self):
        favorite_jobs = FavoritesVacancies.objects.filter(user=self.request.user.id).values('job')
        jobs_ids = [x['job'] for x in favorite_jobs]
        return Job.objects.filter(pk__in=jobs_ids).exclude(status=9)
