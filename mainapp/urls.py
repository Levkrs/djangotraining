from django.urls import path

from .views import Index, login, register,forget_pass


app_name = 'mainapp'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forget-pass/', forget_pass, name='forget-pass'),
]
