from django.urls import path
from .views import ModerListPage

app_name = 'moderapp'

urlpatterns = [
    path('', ModerListPage.as_view(), name='moder_list_page'),

]
