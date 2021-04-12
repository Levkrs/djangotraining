from django.db import models

from authapp.models import MyUser
from companyapp.models import Job


# class MessengerModel(models.Model):
#
#     class Meta:
#         verbose_name = 'MSG'
#
#
#     vacansy = models.ForeignKey(to=Job,on_delete=models.CASCADE, null=False)
#     msg_from = models.ForeignKey(to=MyUser,on_delete=models.CASCADE, null=False)
#     msg_to = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, null=False)
#     msg_text = models.CharField('Текст сообщения', max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


# class InviteRecrut(models.Model):
#
#     class Meta:
#         verbose_name = 'Отклик на вакансию.'
#
#     STATUS = (
#         ('0', 'На рассмотрении'),
#         ('1', 'Принят'),
#         ('2', 'Отклонен'),
#     )
#
#
#     applicant = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, null=False)
#     vacansy = models.ForeignKey(to=Job, on_delete=models.CASCADE, null=False)
#     resume = models.ForeignKey(to=Resume, on_delete=models.CASCADE, null=False)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     status = models.CharField('Статус', max_length=1, choices=STATUS, default='0', db_index=True)
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')