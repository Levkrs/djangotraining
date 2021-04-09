from django.urls import path

from .views import Index, AllNews, NewsDetail, InviteView, InviteFromHr, statusInviteUpdate

app_name = 'mainapp'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('news/', AllNews.as_view(), name='news_all'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('ivnite/<int:job_id>/', InviteView.as_view(), name='invite_user'),
    path('invetofromhr/<int:resume>/', InviteFromHr.as_view(), name='invite_from_hr'),
    path('statusinvupdate/<int:inv_id>/', statusInviteUpdate, name='status_invite_update')
]
