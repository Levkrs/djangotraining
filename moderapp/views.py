from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.views.generic import TemplateView, UpdateView, CreateView

from applicantapp.models import Resume, Education, Experience
from companyapp.models import Job, Company
from moderapp.forms import ResumeModerateForm, JobModerateForm, CompanyModerateForm, AddUpdateNewsForm
from authapp.permissions import ModeratorPermissionMixin
from moderapp.models import News


class ModerListPage(LoginRequiredMixin, ModeratorPermissionMixin, TemplateView):
    """
    Moderator main page
    """
    template_name = 'moderapp/moder_main_page.html'

    def get_context_data(self, **kwargs):
        context = super(ModerListPage, self).get_context_data(**kwargs)
        context['news'] = News.objects.all().order_by('-created_at')
        context['resume_for_aprove'] = Resume.objects.filter(status=2)
        context['job_for_aprove'] = Job.objects.filter(status=2)
        context['company_for_aprove'] = Company.objects.filter(status=2)
        return context


class AddNews(LoginRequiredMixin, ModeratorPermissionMixin, CreateView):
    """
    Adding news
    """
    model = News
    form_class = AddUpdateNewsForm
    template_name = 'moderapp/add_news.html'
    success_url = '/moder'


class UpdateNews(LoginRequiredMixin, ModeratorPermissionMixin, UpdateView):
    """
    Read news details and update
    """
    model = News
    form_class = AddUpdateNewsForm
    template_name = 'moderapp/news_datail.html'
    success_url = '/moder'


class ModerateResume(LoginRequiredMixin, ModeratorPermissionMixin, UpdateView):
    """
    Moderate Resume
    """
    model = Resume
    form_class = ResumeModerateForm
    template_name = 'moderapp/obj_datail.html'
    success_url = '/moder'

    def get_context_data(self, **kwargs):
        data = super(ModerateResume, self).get_context_data(**kwargs)

        EducationFormSet = inlineformset_factory(
            Resume, Education, form=ResumeModerateForm, extra=1)
        ExperienceFormSet = inlineformset_factory(
            Resume, Experience, form=ResumeModerateForm, extra=1)

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


class ModerateJob(LoginRequiredMixin, ModeratorPermissionMixin, UpdateView):
    """
    Moderate Job
    """
    model = Job
    form_class = JobModerateForm
    template_name = 'moderapp/obj_datail.html'
    success_url = '/moder'


class ModerateCompany(LoginRequiredMixin, ModeratorPermissionMixin, UpdateView):
    """
    Moderate Company
    """
    model = Company
    form_class = CompanyModerateForm
    template_name = 'moderapp/obj_datail.html'
    success_url = '/moder'
