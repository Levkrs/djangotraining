"""
Views of applicant
"""
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from applicantapp.forms import ResumeUpdateForm, JobSearchForm
from applicantapp.models import Resume
from authapp.models import MyUser
from companyapp.models import Job
from authapp.permissions import PERMISSION_DENIED_MESSAGE, ApplicantPermissionMixin
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
    fields = ('headline', 'status', 'first_name', 'surname', 'salary', 'date_of_birth', 'city', 'user_pic', 'links', 'employment', 'work_schedule', 'education_type', 'about_me', 'key_skills', 'phone')
    template_name = 'applicantapp/create_resume.html'

    def get_success_url(self):
        return reverse_lazy('applicantapp:profile', args=(self.request.user.id,))

    def form_valid(self, form):
        user_for_reg = MyUser.objects.get(id=self.request.user.id)
        form.instance.user = user_for_reg
        return super(CreateResume, self).form_valid(form)


class UpdateResume(LoginRequiredMixin, ApplicantPermissionMixin, UpdateView):
    """
    Update Resume
    """
    model = Resume
    form_class = ResumeUpdateForm
    template_name = 'applicantapp/update_resume.html'
    success_url = '/'

    def form_valid(self, form):
        ctx = super(UpdateResume, self).form_valid(form)
        user_for_reg = MyUser.objects.get(id=self.request.user.id)
        form.instance.user = user_for_reg
        return super(UpdateResume, self).form_valid(form)


class JobListDetail(LoginRequiredMixin, DetailView):
    """
    Развернуть резюме подробнро
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
                QUERY.append((Q(description__icontains=field) | Q(short_description__icontains=field)))
            elif field_name == 'city' and field:
                QUERY.append(Q(city__icontains=field))
            elif field and field != '':
                QUERY.append(Q(**{field_name: field}))


        if any(QUERY):
            object_list = Job.objects.filter(*QUERY)
            return object_list

        return Job.objects.filter(status='3')



class ResponceHr(ListView):
    """
    Приглащения от HR
    """

    model = FullInvite
    template_name = 'applicantapp/responce_hr.html'


    def get_queryset(self):
        resume_list_id = list(Resume.objects.filter(user=self.request.user.id).values_list('id', flat=True))
        object_list = FullInvite.objects.filter(recrut_resume_id__in=resume_list_id).filter(aprove_recrut=False)
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