from django.urls import path

from .views import ProfileView, CompanyDetailView, CompanyUpdateView, JobListView

app_name = 'companyapp'

urlpatterns = [
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/card/', CompanyDetailView.as_view(), name='card'),
    path('<int:pk>/card/edit', CompanyUpdateView.as_view(), name='edit'),
    path('job-list', JobListView.as_view(), name='job-list'),
]
