from django.urls import path

from .views import Login, Logout, register, forget_pass


app_name = 'authapp'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('forget-pass/', forget_pass, name='forget-pass'),
]
