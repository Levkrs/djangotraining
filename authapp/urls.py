from django.urls import path

from .views import login, register, forget_pass


app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forget-pass/', forget_pass, name='forget-pass'),
]
