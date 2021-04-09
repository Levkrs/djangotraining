from django.urls import path

from .views import (
    ProfileView, CompanyDetailView, CompanyUpdateView, JobCreateView, JobDetailView,
    JobUpdateView, JobListView, ResumeListHR, ResumeListDetail, ResumeSearchList, ResponceRec, RespJobDetail
)


app_name = 'companyapp'

urlpatterns = [
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/card/', CompanyDetailView.as_view(), name='card'),
    path('<int:pk>/card/edit/', CompanyUpdateView.as_view(), name='edit'),
    path('<int:pk>/job/new/', JobCreateView.as_view(), name='new-job'),
    path('job/<int:pk>/edit/', JobUpdateView.as_view(), name='edit-job'),
    path('job/<int:pk>/detail/', JobDetailView.as_view(), name='detail-job'),
    path('job-list/', JobListView.as_view(), name='job-list'),
    path('resume-list/', ResumeListHR.as_view(), name='resume-list'),
    path('resume-detail/<int:pk>/', ResumeListDetail.as_view(), name='resume-list-detail'),
    path('resume-search/', ResumeSearchList.as_view(), name='resume_search'),
    path('responce-rec/', ResponceRec.as_view(), name='responce_recrut_list'),
    path('responce/<int:pk>/detail/<int:inv_id>/', RespJobDetail.as_view(), name='responce_job_detail'),

]