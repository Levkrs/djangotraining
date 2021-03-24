from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView

from applicantapp.models import Resume
from companyapp.models import Job, Company


class ModerListPage(TemplateView):
    template_name = 'moderapp/moder_main_page.html'

    def get_context_data(self, **kwargs):
        context = super(ModerListPage, self).get_context_data(**kwargs)
        context['resume_for_aprove'] = Resume.objects.filter(status=2)
        context['job_for_aprove'] = Job.objects.filter(status=2)
        context['company_for_aprove'] = Company.objects.filter(status=2)
        return context



