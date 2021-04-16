from django.urls import path

from messenger.views import DialogList, DialogDetail, create_message

app_name = 'messenger'

urlpatterns = [
    path('dialog_list/', DialogList.as_view(), name='dialog_list'),
    path('dialog_detail/<int:pk>', DialogDetail.as_view(), name='dialog_detail'),
    path('create_msg/<int:pk>', create_message, name='create_message'),


]
