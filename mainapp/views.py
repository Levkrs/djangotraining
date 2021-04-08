from django.views.generic import TemplateView, ListView, DetailView

from moderapp.models import News


class Index(TemplateView):
    """
    Главная страница
    """
    template_name = 'mainapp/index.html'
    extra_context = {
        'title_name': 'GeekStaff',
        'news': News.objects.all().order_by('-created_at')[:5],
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
