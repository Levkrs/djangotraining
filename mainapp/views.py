from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from authapp.models import MyUser
from companyapp.models import Job, Company
from mainapp.forms import IviteForm, InviteFromHrForm
from moderapp.models import News
from mainapp.models import InviteRecrut
from applicantapp.models import Resume



class Index(TemplateView):
    """
    Главная страница
    """
    template_name = 'mainapp/index.html'
    extra_context = {
        'title_name': 'GeekStaff',
        'news': News.objects.all().order_by('-created_at'),
    }


class InviteView(CreateView):
    """ Отклик на вакансию """
    form_class = IviteForm
    template_name = 'mainapp/inve_form.html'
    success_url = reverse_lazy('mainapp:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'].fields['resume'].queryset = Resume.objects.filter(user=self.request.user.pk).filter(status=3)
        return ctx

    def form_valid(self, form):
        print('asd')
        vac = Job.objects.filter(id=self.kwargs['job_id']).first()
        _user = MyUser.objects.get(id=self.request.user.id)
        form.instance.applicant = _user
        form.instance.vacansy = vac
        return super(InviteView, self).form_valid(form)

class InviteFromHr(CreateView):
    """Отклики на резюме"""
    form_class = InviteFromHrForm
    template_name = "mainapp/inve_form.html"
    success_url = reverse_lazy('mainapp:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        company = Company.objects.get(user=self.request.user)
        ctx['form'].fields['vacansy'].queryset = Job.objects.filter(company_id=company.id).filter(status=3)
        return ctx

    def form_valid(self, form):
        print('asd')
        _resume = Resume.objects.filter(id=self.kwargs['resume']).first()
        _company = Company.objects.get(user=self.request.user)
        form.instance.hr = _company
        form.instance.resume = _resume
        return super(InviteFromHr, self).form_valid(form)




