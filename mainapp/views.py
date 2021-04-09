from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from applicantapp.models import Resume
from authapp.models import MyUser
from companyapp.models import Job, Company
from mainapp.forms import IviteForm, InviteFromHrForm
from mainapp.models import InviteHr, InviteRecrut
from moderapp.models import News


class Index(TemplateView):
    """
    Главная страница
    """
    template_name = 'mainapp/index.html'
    extra_context = {
        'title_name': 'GeekStaff',
        'object_list': News.objects.all().order_by('-created_at')[:3]
    }


class AllNews(ListView):
    """
    All news
    """
    template_name = 'mainapp/news_all.html'

    def get_queryset(self):
        return News.objects.all().order_by('-created_at')


class NewsDetail(DetailView):
    """
    Detail of some news item
    """
    model = News
    template_name = 'mainapp/news_detail.html'

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


def statusInviteUpdate(request, inv_id):
    if request.method == 'POST':
        print('POST')
        if request.user.role == "REC":
            object_inv = InviteHr.objects.get(id=inv_id)
            resume = object_inv.resume
            status = request.POST['status']
            if resume.user_id == request.user.id:
                object_inv.status = request.POST['status']
                object_inv.save()
        elif request.user.role == "HR":
            object_inv = InviteRecrut.objects.get(id=inv_id)
            job = object_inv.vacansy
            if job.company.user.pk == request.user.pk:
                object_inv.status = request.POST['status']
                object_inv.save()
        else:
            pass
        return HttpResponseRedirect(reverse('mainapp:index'))


