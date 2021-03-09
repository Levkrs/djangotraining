from django.db import models

from authapp.models import MyUser


class Company(models.Model):
    """
    Компания-работодатель
    """
    def user_directory_path(instance, filename):
        return f'logo/user_{instance.user_id.id}/{filename}'

    user_id = models.OneToOneField(to=MyUser, on_delete=models.PROTECT, related_name='company', verbose_name="user's id")
    name = models.CharField('Наименование компании', max_length=255, blank=False, db_index=True)
    logo = models.ImageField('Логотип', upload_to=user_directory_path)
    headline = models.CharField('Слоган', max_length=255, blank=True)
    short_description = models.CharField('Краткое описание', max_length=255, blank=False)
    detail = models.TextField('Подробное описание', blank=True)
    location = models.CharField('Местонахождение', max_length=255, blank=False)
    link = models.CharField('Ссылка на сайт / соц.сеть', max_length=255, blank=True)
    is_active = models.BooleanField('Профиль компании активен', blank=False, default=False)
    is_cheked = models.BooleanField('Проверена модератором', blank=False, default=False)
    moder_comment = models.TextField('Заключение модератора', blank=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Job(models.Model):
    """
    Вакансии
    """
    company_id = models.ForeignKey(to=Company, on_delete=models.PROTECT, related_name='jobs', verbose_name='ID компании')
    is_active = models.BooleanField('Вакансия активна', blank=False, default=False)
    is_cheked = models.BooleanField('Проверена модератором', blank=False, default=False)
    moder_comment = models.TextField('Заключение модератора', blank=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
