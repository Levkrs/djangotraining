from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from applicantapp.models import Resume
from authapp.models import MyUser
from companyapp.models import Job, Company
from mainapp.forms import FullInviteForm, FullInviteFormUser
from mainapp.models import FullInvite
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
    form_class = FullInviteFormUser
    template_name = 'mainapp/inve_form.html'
    success_url = reverse_lazy('mainapp:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'].fields['recrut_resume'].queryset = Resume.objects.filter(user=self.request.user.pk).filter(status=3)
        return ctx

    def form_valid(self, form):
        _recrut = Resume.objects.filter(id=form.data['recrut_resume']).first()
        _job = Job.objects.get(id=self.kwargs['job_id'])
        form.instance.hr = _job.company
        form.instance.recrut_resume = _recrut
        form.instance.vacansy = _job
        form.instance.aprove_recrut = True
        if (len(FullInvite.objects.
                       filter(vacansy=_job).filter(hr=_job.company).
                       filter(recrut_resume=_recrut).
                       filter(aprove_recrut=1))!= 0 ):
            # return super(InviteView, self).form_valid(form)
            # form.add_error(None, {"recrut_resume": "element is exist"})
            return HttpResponseRedirect(reverse('applicantapp:job-list-detail',kwargs={'pk':_job.pk}))
        else:
            print('---')

            return super(InviteView, self).form_valid(form)


class InviteFromHr(CreateView):
    """Отклики на резюме"""
    form_class = FullInviteForm
    # model = FullInvite
    template_name = "mainapp/inve_form.html"
    success_url = reverse_lazy('mainapp:index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        company = Company.objects.get(user=self.request.user)
        ctx['form'].fields['vacansy'].queryset = Job.objects.filter(company_id=company.id).filter(status=3)
        return ctx

    def form_valid(self, form):
        _recrut = Resume.objects.filter(id=self.kwargs['resume']).first()
        _company = Company.objects.get(user=self.request.user)
        _id_vacansy = form.data['vacansy']
        form.instance.hr = _company
        form.instance.recrut_resume = _recrut
        # if (self.request.user.role == 'HR'):
        form.instance.aprove_hr = True
        # elif (self.request.user.role == "REC"):
        #     form.instance.aprove_recrut = True
        # else:
        #     return reverse_lazy('mainapp:index')
        last_inv = FullInvite.objects.filter(vacansy=_id_vacansy)
        print(last_inv)

        if (len(FullInvite.objects.
                        filter(vacansy=_id_vacansy).filter(hr=_company).
                        filter(recrut_resume=_recrut).
                        filter(aprove_hr=1)) != 0):
            return HttpResponseRedirect(reverse('companyapp:resume-list-detail', kwargs={'pk': _id_vacansy}))
        else:
            print('---')
            return super(InviteFromHr, self).form_valid(form)
        # invite_len = len(FullInvite.objects.filter(recrut_resume=_recrut).filter(hr=_company).filter(vacansy=_id_vacansy))
        # print(invite_len)
        # if invite_len != 0:
        #     print('Уж создано')
        # return super(InviteFromHr, self).form_valid(form)




def statusInviteUpdate(request, pk):
    '''Тестовая версия'''
    if request.method == 'POST':
        print('POST')
        role_ = request.user.role
        if request.user.role == "REC":
            _vacansy = Job.objects.get(id=pk)
            recrut_resume= Resume.objects.filter(user=request.user)
            invite_objects = FullInvite.objects.filter(vacansy=_vacansy).filter(recrut_resume__in=recrut_resume).filter(aprove_recrut=0).first()
            invite_objects.aprove_recrut = request.POST['status']
            invite_objects.save()
        elif request.user.role == "HR":
            _resume = Resume.objects.get(id=pk)
            invite_objects = FullInvite.objects.filter(recrut_resume=_resume).filter(aprove_hr=0).first()
            invite_objects.aprove_hr = request.POST['status']
            invite_objects.save()
        return HttpResponseRedirect(reverse('mainapp:index'))


