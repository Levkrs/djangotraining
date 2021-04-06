from django.views.generic import TemplateView

from moderapp.models import News


class Index(TemplateView):
    """
    Главная страница
    """
    template_name = 'mainapp/index.html'
    extra_context = {
        'title_name': 'GeekStaff',
        'news': News.objects.all().order_by('-created_at'),
    }
