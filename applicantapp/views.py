"""
Views of applicant
"""
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

from applicantapp.forms import UserProfileForm, ResumeUpdateForm
from applicantapp.models import Resume, StatusResume
from authapp.models import MyUser
from companyapp.models import Job
from authapp.permissions import PERMISSION_DENIED_MESSAGE, ApplicantPermissionMixin
# from icecream import ic
# from django.db.models import Q
from mainapp.models import InviteHr


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    ЛК Соискателя
    """
    template_name = 'applicantapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_list'] = Resume.objects.filter(user=self.request.user.pk)
        return context


class ResumeList(LoginRequiredMixin, ListView):
    """
    Список резюме пользователя
    """
    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user.id)


class CreateResume(LoginRequiredMixin, ApplicantPermissionMixin, CreateView):
    """
    Создание резюме
    """
    form_class = UserProfileForm
    template_name = 'applicantapp/create_resume.html'


    def get_success_url(self):
        print(self.object.id)
        return reverse_lazy('applicantapp:profile', args=(self.request.user.id,))

    def get_context_data(self, **kwargs):
        ctx = super(CreateResume, self).get_context_data(**kwargs)
        return ctx

    def form_valid(self, form):
        user_for_reg = MyUser.objects.get(id=self.request.user.id)
        form.instance.user = user_for_reg

        return super(CreateResume, self).form_valid(form)

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        return super(CreateResume, self).post(request, **kwargs)

class UpdateResume(LoginRequiredMixin, ApplicantPermissionMixin, UpdateView):
    """
    Update Resume
    """
    model = Resume
    form_class = ResumeUpdateForm
    template_name = 'applicantapp/update_resume.html'
    success_url = '/'

    def form_valid(self, form):
        ctx = super(UpdateResume, self).form_valid(form)
        user_for_reg = MyUser.objects.get(id=self.request.user.id)
        form.instance.user = user_for_reg
        # if form.data['submit_btn_val']:
        #     name_status = form.data['submit_btn_val']
        #     status_val = StatusResume.objects.get(id=name_status)
        #     form.instance.status = status_val.status_name
        return super(UpdateResume, self).form_valid(form)

# class JobSearchList(LoginRequiredMixin, ListView):
#
#     model = Job
#     template_name = 'applicantapp/job_search.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             object_list = Job.objects.filter(
#                 Q(description__icontains=query) | Q(short_description__icontains=query)
#             )
#             return object_list
#         else:
#             return Job.objects.all()


class JobListDetail(LoginRequiredMixin, DetailView):
    """
    Развернуть резюме подробнро
    """

    model = Resume

    template_name = 'applicantapp/job_detail.html'

    def get_queryset(self):
        req = Job.objects.filter(pk=self.kwargs['pk'])


        # CHOISE = Job()
        # a = 'FED'
        # result = filter(a, for iter in CHOISE.CATEGORY)
        # result = filter(lambda x: x[0] == a, CHOISE.CATEGORY)
        # ic(CHOISE.)
        # ic(req.__dict__)
        # for item in req:
            # ic(item.__dict__)
            # ic(item.category)
            # cat_status = item.category
            # get_category_name = list(filter(lambda x: x[0] == cat_status, item.CATEGORY))
            # ic(get_category_name)
            # item.category = get_category_name[0][1]
            # ic(item.category)
            # cat_choise = item['category']
            # get_choise_name = filter(lambda x: x[0] == a, CHOISE.CATEGORY)
            # item['category'] = get_choise_name
            # ic(item.CATEGORY)
        return req

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # obj = context['object']
        # obj.category = 'ASDSAD'
        # ic(context['object'].__dict__)
        return context

class JobSearchList(ListView):
    """Поиск вакансий по краткому описанию"""
    model = Job
    template_name = 'applicantapp/job_search.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Job.objects.filter(
                Q(description__icontains=query) | Q(short_description__icontains=query)
            )
            return object_list
        else:
            return Job.objects.all()

class ResponceHr(ListView):
    model = InviteHr
    template_name = 'applicantapp/responce_hr.html'


    def get_queryset(self):
        # company_to_user = self.request.user.company.id
        # print(company_to_user)
        resume_list_id = list(Resume.objects.filter(user=self.request.user.id).values_list('id', flat=True))
        object_list = InviteHr.objects.filter(resume_id__in=resume_list_id)
        print('__')

        return object_list