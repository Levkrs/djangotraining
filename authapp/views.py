from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import MyUserCreationForm


class SignUp(CreateView):
    """ Регистрация нового пользователя """
    form_class = MyUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('authapp:login')


class Login(UserPassesTestMixin, LoginView):
    def test_func(self):
        return not self.request.user.is_authenticated


class Logout(LoginRequiredMixin, LogoutView):
    def get_next_page(self):
        return super().get_next_page()


def forget_pass(request):
    return render(request, 'authapp/user-forget-pass.html')
