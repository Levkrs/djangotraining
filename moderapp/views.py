from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView

from applicantapp.models import Resume
from companyapp.models import Job, Company
from moderapp.forms import ResumeForChecked


class ModerListPage(TemplateView):
    # model = Resume
    template_name = 'moderapp/moder_main_page.html'


    def get_context_data(self, **kwargs):
        context = super(ModerListPage, self).get_context_data(**kwargs)
        context['resume_for_aprove'] = Resume.objects.filter(is_cheked=False)
        context['job_for_aprove'] = Job.objects.filter(status=2)
        context['company_for_aprove'] = Company.objects.filter(status=2)

        return context


# class CheckedResumePage(DetailView):
#     model = Resume
#     # form_class = ResumeForChecked
#     template_name = 'moderapp/moder_resume_detail.html'
#     success_url = '/'
#
#     def get_context_data(self, **kwargs):
#         context = super(CheckedResumePage, self).get_context_data(**kwargs)
#         print('For aprove')
#         return context
#
# class JobUpdateView(LoginRequiredMixin, UpdateView):
#     """ Редактор карточки вакансии """
#     model = Job
#     fields = ('status', 'grade', 'category', 'salary', 'city', 'employment', 'skills',
#               'work_schedule', 'experience', 'short_description', 'description',)

# class CheckedResumePage(UpdateView):
#     """
#     Checked Resume
#     """
#     model = Resume
#     form_class = ResumeForChecked
#     template_name = 'moderapp/moder_resume_detail.html'
#     success_url = '/'
#
#     # def get_success_url(self):
    #     return reverse_lazy('companyapp:card', args=[self.object.pk])

class CheckedResumePage(UpdateView):
    model = Resume
    fields = '__all__'
    template_name = 'moderapp/moder_resume_detail.html'
    # success_url = '/'

    def get_success_url(self):
        return reverse('moderapp:moder_list_page')


class CheckJobPage(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'moderapp/moder_job_detail.html'

    def get_success_url(self):
        return reverse('moderapp:moder_list_page')