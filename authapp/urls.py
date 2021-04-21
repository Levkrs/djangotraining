from django.urls import path

from .views import SignUp, Login, Logout


app_name = 'authapp'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
