from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from companyapp.models import Job


class Index(TemplateView):
    """
    Главная страница
    """    
    template_name = 'mainapp/index.html'
    extra_context = {'title_name': 'GeekStaff'}


class JobSearchList(ListView):
    """Поиск вакансий по краткому описанию"""
    model = Job
    template_name = 'mainapp/job_search.html'
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


    