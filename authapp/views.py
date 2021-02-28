from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


class Login(UserPassesTestMixin, LoginView):
    def test_func(self):
        return not self.request.user.is_authenticated


class Logout(LoginRequiredMixin, LogoutView):
    def get_next_page(self):
        return super().get_next_page()


def register(request):
    return render(request, 'authapp/user-register.html')


def forget_pass(request):
    return render(request, 'authapp/user-forget-pass.html')
