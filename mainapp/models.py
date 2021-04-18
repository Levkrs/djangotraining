from django.db import models

from authapp.models import MyUser
from companyapp.models import Job, Company
from applicantapp.models import Resume

# Create your models here.

class FullInvite(models.Model):

    class Meta:
        verbose_name= 'Общий отклик'

    vacansy = models.ForeignKey(to=Job, on_delete=models.CASCADE, null=False)
    hr = models.ForeignKey(to=Company, on_delete=models.CASCADE, null=False)
    recrut_resume = models.ForeignKey(to=Resume, on_delete=models.CASCADE, null=False)
    aprove_hr = models.BooleanField('Aprove от hr', default=False)
    aprove_recrut = models.BooleanField('Aprove от рекрута', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
