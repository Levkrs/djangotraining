"""
Views of applicant
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from applicantapp.models import Resume


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    ЛК Соискателя
    """
    template_name = 'applicantapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ResumeList(LoginRequiredMixin, ListView):
    """
    List of applicants resumes
    """
    def get_queryset(self):
        return Resume.objects.filter(user_id=self.request.user.id)
