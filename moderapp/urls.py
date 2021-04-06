from django.urls import path
from .views import ModerListPage, ModerateResume, ModerateCompany, ModerateJob, AddNews, UpdateNews

app_name = 'moderapp'

urlpatterns = [
    path('', ModerListPage.as_view(), name='moder_list_page'),
    path('add_news', AddNews.as_view(), name='add_news'),
    path('update_news/<int:pk>/', UpdateNews.as_view(), name='update_news'),
    path('moderate_resume/<int:pk>/', ModerateResume.as_view(), name='moderate_resume'),
    path('moderate_job/<int:pk>/', ModerateJob.as_view(), name='moderate_job'),
    path('moderate_company/<int:pk>/', ModerateCompany.as_view(), name='moderate_company'),
]
