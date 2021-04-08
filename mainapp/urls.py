from django.urls import path

from .views import Index, AllNews, NewsDetail

app_name = 'mainapp'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('news/', AllNews.as_view(), name='news_all'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
]
