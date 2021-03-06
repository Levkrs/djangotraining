"""
Models for applicant
"""

from django.db import models

from authapp.models import MyUser


class Resume(models.Model):
    """
    Applicants resume
    """

    class Meta:
        get_latest_by = '-updated_at'
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    EMPLOYMENT_CHOICES = (
        ('FT', 'Полная занятость'),
        ('PT', 'Частичная занятость'),
        ('PW','Проектная работа'),
        ('VL','Волонтерство'),
        ('WP','Стажировка'),
    )

    WORK_SCHEDULE_CHOICES = (
        ('FD', 'Полный день'),
        ('SSCH', 'Сменный график'),
        ('FSCH', 'Гибкий график'),
        ('RW', 'Удаленная работа'),
        ('RBW', 'Вахтовый метод'),
    )

    EDUCATION_CHOICES = (
        ('SECONDARY', 'Среднее'),
        ('SPECIAL_SECONDARY','Среднее специальное'),
        ('UNFINISHED_HIGHER','Неоконченное высшее'),
        ('HIGHER', 'Высшее'),
        ('BACHELOR','Бакалавр'),
        ('MASTER', 'Магистр'),
        ('CANDIDATE', 'Кандидат наук'),
        ('DOCTOR', 'Доктор наук'),
    )

    user_id = models.ForeignKey(to=MyUser, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, null=False, verbose_name='Заголовок')
    first_name = models.CharField(max_length=255, null=False, verbose_name='Имя')
    surname = models.CharField(max_length=255, null=False, verbose_name='Фамилия')
    salary = models.PositiveIntegerField(null=True, verbose_name='Желаемая заработная плата')
    date_of_birth = models.DateField(null=False, verbose_name='Дата рождения')
    is_active = models.BooleanField(null=False, default=False, verbose_name='Резюме активно')
    is_cheked = models.BooleanField(null=False, default=False, verbose_name='Резюме проверенно модератором')
    city = models.CharField(max_length=255, null=False, verbose_name='Город')
    user_pic = models.ImageField(upload_to='media/photo', height_field=200, width_field=200, verbose_name='Фото')
    links = models.CharField(max_length=255, null=True, verbose_name='Ссылка на профиль в соц. сетях или сайт')
    employment = models.CharField(max_length=20, null=False, choices=EMPLOYMENT_CHOICES, default='FT', verbose_name='Занятость')
    work_schedule = models.CharField(max_length=20, null=False, choices=WORK_SCHEDULE_CHOICES, default='FD', verbose_name='График работы')
    education_type = models.CharField(max_length=20, null=False, choices=EDUCATION_CHOICES, default='HIGHER', verbose_name='Образование')
    about_me = models.TextField(null=True, verbose_name='Обо мне')
    key_skills = models.CharField(max_length=255, null=True, verbose_name='Ключевые навыки')
    phone = models.CharField(max_length=20, null=False, verbose_name='Телефон')
    moder_comment = models.TextField(null=True, verbose_name='Комментарий модератора')
    views_count = models.PositiveIntegerField(null=False, default=0, verbose_name='Кол-во просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __repr__(self):
        return self.headline

    def __str__(self):
        return self.headline


class Education(models.Model):
    """
    Applicant education institutions
    """

    class Meta:
        get_latest_by = '-id'
        verbose_name = 'Образовательное учреждение'
        verbose_name_plural = 'Образовательные учреждения'

    resume_id = models.ForeignKey(to=Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, verbose_name='Название учреждения')
    specialization = models.CharField(max_length=255, null=False, verbose_name='Специальность')
    year_of_ending = models.PositiveIntegerField(null=False, verbose_name='Год окончания')


class Experience(models.Model):
    """
    Applicant work experience
    """

    class Meta:
        get_latest_by = '-id'
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    resume_id = models.ForeignKey(to=Resume, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, null=False, verbose_name='Название компании')
    company_link = models.CharField(max_length=255, null=True, verbose_name='Сайт компании')
    position = models.CharField(max_length=255, null=False, verbose_name='Дожность')
    data_from = models.DateField(null=False, verbose_name='Дата начала работы')
    data_to = models.DateField(null=False, verbose_name='Дата окончания работы')
    description = models.TextField(null=True, verbose_name='Описание')