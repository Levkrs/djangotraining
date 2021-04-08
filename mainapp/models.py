from django.db import models
from django.utils import timezone

from authapp.models import MyUser
from companyapp.models import Job, Company
from applicantapp.models import Resume

# Create your models here.
class InviteRecrut(models.Model):

    class Meta:
        verbose_name = 'Отклик на вакансию.'


    applicant = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, null=False)
    vacansy = models.ForeignKey(to=Job, on_delete=models.CASCADE, null=False)
    resume = models.ForeignKey(to=Resume, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    # def __str__(self):
    #     return self.applicant.email



class InviteHr(models.Model):

    class Meta:
        verbose_name = 'Отклик на резюме.'

    hr = models.ForeignKey(to=Company, on_delete=models.CASCADE, null=False)
    vacansy = models.ForeignKey(to=Job, on_delete=models.CASCADE, null=False)
    resume = models.ForeignKey(to=Resume, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')