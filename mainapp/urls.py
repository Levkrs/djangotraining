from django.urls import path

from .views import Index, JobSearchList


app_name = 'mainapp'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('job_search/', JobSearchList.as_view(), name='job_search')
]
