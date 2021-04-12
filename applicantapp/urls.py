"""
Urls for applicant
"""
from django.urls import path

from applicantapp.views import (
    ProfileView, ResumeList, CreateResume, UpdateResume, JobListDetail, JobSearchList, ResponceHr,
    ResponceJobDetail
)


app_name = 'applicantapp'

urlpatterns = [
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('createresume/', CreateResume.as_view(), name='createresume'),
    path('resume-list/', ProfileView.as_view(), name='resume-list'),
    path('resumes-list/update_resume/<int:pk>/', UpdateResume.as_view(), name='update_resume'),
    path('job-search-list/', JobSearchList.as_view(), name='job_search_list'),
    path('job-detail/<int:pk>/', JobListDetail.as_view(), name='job-list-detail'),
    path('responce-job/', ResponceHr.as_view(), name='responce_resume_list'),
    path('responce-job-detail/<int:pk>/', ResponceJobDetail.as_view(), name='respince_job_detail')

]
