from django.urls import path
from .views import ModerListPage, CheckedResumePage, CheckJobPage

app_name = 'moderapp'

urlpatterns = [
    path('', ModerListPage.as_view(), name='moder_list_page'),
    path('resume_aprove/<int:pk>', CheckedResumePage.as_view(), name='resume_for_aprove'),
    path('job_aprove/<int:pk>', CheckJobPage.as_view(), name='job_for_aprove'),
]
