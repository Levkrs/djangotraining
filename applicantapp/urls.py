"""
Urls for applicant
"""

from django.urls import path

from applicantapp.views import ResumeList

app_name = 'applicantapp'

urlpatterns = [
    path('resumes', ResumeList.as_view(), name='resumes')
]
