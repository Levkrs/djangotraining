"""
Views of applicant
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView
from applicantapp.forms import UserProfileForm
from applicantapp.models import Resume
from authapp.models import MyUser


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    ЛК Соискателя
    """
    template_name = 'applicantapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ResumeList(LoginRequiredMixin, ListView):
    """
    List of applicants resumes
    """
    def get_queryset(self):
        return Resume.objects.filter(user_id=self.request.user.id)


class CreateResume(LoginRequiredMixin, CreateView):
    """
    Создание резюме
    """
    form_class = UserProfileForm
    template_name = 'applicantapp/create_resume.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        ctx = super(CreateResume, self).get_context_data(**kwargs)
        return ctx

    def form_valid(self, form):
        user_for_reg = MyUser.objects.get(id=self.request.user.id)
        form.instance.user_id = user_for_reg
        return super(CreateResume, self).form_valid(form)
    #
    # def from_invalid(self, form):
    #     text=form
    #     ic(form)
    #     return super(CreateResume, self).from_invalid(form)
    #
    # def post(self, request, **kwargs):
    #     request.POST = request.POST.copy()
    #     ic(request.POST)
    #     # request.POST['owner'] = 2
    #     return super(CreateResume, self).post(request, **kwargs)

