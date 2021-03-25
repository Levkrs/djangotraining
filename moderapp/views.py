from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView
from django.views.generic import ListView, TemplateView, UpdateView

from applicantapp.models import Resume
from companyapp.models import Job, Company
from moderapp.forms import ResumeModerateForm, JobModerateForm, CompanyModerateForm


class ModerListPage(LoginRequiredMixin, TemplateView):
    template_name = 'moderapp/moder_main_page.html'

    def get_context_data(self, **kwargs):
        context = super(ModerListPage, self).get_context_data(**kwargs)
        context['resume_for_aprove'] = Resume.objects.filter(status=2)
        context['job_for_aprove'] = Job.objects.filter(status=2)
        context['company_for_aprove'] = Company.objects.filter(status=2)
        return context

class CheckedResumePage(UpdateView):
    model = Resume
    fields = '__all__'
    template_name = 'moderapp/moder_resume_detail.html'
    # success_url = '/'

    def get_success_url(self):
        return reverse('moderapp:moder_list_page')


class ModerateResume(LoginRequiredMixin, UpdateView):
    """
    Moderate Resume
    """
    model = Resume
    form_class = ResumeModerateForm
    template_name = 'moderapp/obj_datail.html'
    success_url = '/moder'


class ModerateJob(LoginRequiredMixin, UpdateView):
    """
    Moderate Job
    """
    model = Job
    form_class = JobModerateForm
    template_name = 'moderapp/obj_datail.html'
    success_url = '/moder'


class ModerateCompany(LoginRequiredMixin, UpdateView):
    """
    Moderate Company
    """
    model = Company
    form_class = CompanyModerateForm
    template_name = 'moderapp/obj_datail.html'
    success_url = '/moder'


class CheckJobPage(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'moderapp/moder_job_detail.html'

    def get_success_url(self):
        return reverse('moderapp:moder_list_page')