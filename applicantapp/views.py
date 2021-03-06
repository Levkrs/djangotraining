"""
Views of applicant
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from applicantapp.models import Resume


class ResumeList(LoginRequiredMixin, ListView):
    """
    List of applicants resumes
    """
    def get_queryset(self):
        return Resume.objects.filter(user_id=self.request.user.id)

