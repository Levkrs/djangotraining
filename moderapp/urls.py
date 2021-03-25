from django.urls import path
from .views import ModerListPage, CheckedResumePage, CheckJobPage
from .views import ModerListPage, ModerateResume, ModerateCompany, ModerateJob

app_name = 'moderapp'

urlpatterns = [
    path('', ModerListPage.as_view(), name='moder_list_page'),
    path('resume_aprove/<int:pk>', CheckedResumePage.as_view(), name='resume_for_aprove'),
    path('job_aprove/<int:pk>', CheckJobPage.as_view(), name='job_for_aprove'),
    path('moderate_resume/<int:pk>/', ModerateResume.as_view(), name='moderate_resume'),
    path('moderate_job/<int:pk>/', ModerateJob.as_view(), name='moderate_job'),
    path('moderate_company/<int:pk>/', ModerateCompany.as_view(), name='moderate_company'),
]
