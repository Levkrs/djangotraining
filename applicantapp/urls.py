"""
Urls for applicant
"""
from django.urls import path

from applicantapp.views import ProfileView, ResumeList, CreateResume


app_name = 'applicantapp'

urlpatterns = [
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('resumes', ResumeList.as_view(), name='resumes'),
    path('createresume',CreateResume.as_view(), name='createresume')
]
