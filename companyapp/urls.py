from django.urls import path

from .views import ProfileView


app_name = 'companyapp'

urlpatterns = [
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
]
