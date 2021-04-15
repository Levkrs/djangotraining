from django.db import models

from authapp.models import MyUser
from companyapp.models import Job


class MessengerModel(models.Model):

    class Meta:
        verbose_name = 'MSG'

    vacansy = models.ForeignKey(to=Job,on_delete=models.CASCADE, null=False, related_name='vacansy_message')
    msg_from = models.ForeignKey(to=MyUser,on_delete=models.CASCADE, null=False, related_name='msg_from')
    msg_to = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, null=False, related_name='msg_to')
    msg_text = models.CharField('Текст сообщения', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
