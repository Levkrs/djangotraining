"""
Models for applicant
"""

from django.db import models

from authapp.models import MyUser


class StatusResume(models.Model):
    class Meta:
        verbose_name = 'Статус Резюме'
        verbose_name_plural = 'Статусы Резюме'

    status_name = models.CharField(max_length=250, blank=True, null=True)

    def __repr__(self):
        return self.status_name

    def __str__(self):
        return self.status_name


class Resume(models.Model):
    """
    Applicants resume
    """
    def user_directory_path(instance, filename):
        return f'resume/user_{instance.user.id}/{filename}'

    class Meta:
        get_latest_by = '-updated_at'
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    STATUS = (
        ('0', 'Отклонено модератором'),
        ('1', 'Заготовка'),
        ('2', 'На модерации'),
        ('3', 'Опубликовано'),
        ('4', 'Черновик'),
        ('5', 'Скрыто'),
        ('9', 'Удалено'),
    )

    EMPLOYMENT_CHOICES = (
        ('FT', 'Полная занятость'),
        ('PT', 'Частичная занятость'),
        ('PW', 'Проектная работа'),
        ('VL', 'Волонтерство'),
        ('WP', 'Стажировка'),
    )

    WORK_SCHEDULE_CHOICES = (
        ('FD', 'Полный день'),
        ('SSCH', 'Сменный график'),
        ('FSCH', 'Гибкий график'),
        ('RW', 'Удаленная работа'),
        ('RBW', 'Вахтовый метод'),
    )

    user = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, null=True)
    headline = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    status = models.CharField('Статус', max_length=1, choices=STATUS, default='1', db_index=True)
    first_name = models.CharField(max_length=255, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=255, blank=False, verbose_name='Фамилия')
    salary = models.PositiveIntegerField(blank=True, null=True, verbose_name='Желаемая заработная плата')
    date_of_birth = models.DateField(blank=False, verbose_name='Дата рождения')
    city = models.CharField(max_length=255, blank=False, verbose_name='Город')
    user_pic = models.ImageField(upload_to=user_directory_path, blank=True,
                                 null=True, verbose_name='Фото')
    links = models.CharField(max_length=255, blank=True, null=True,
                             verbose_name='Ссылка на профиль в соц. сетях или сайт')
    employment = models.CharField(max_length=20, blank=False, choices=EMPLOYMENT_CHOICES,
                                  verbose_name='Занятость')
    work_schedule = models.CharField(max_length=20, blank=False, choices=WORK_SCHEDULE_CHOICES,
                                     verbose_name='График работы')
    about_me = models.TextField(blank=True, null=True, verbose_name='Обо мне')
    key_skills = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ключевые навыки')
    phone = models.CharField(max_length=20, blank=False, verbose_name='Телефон')
    moder_comment = models.TextField(blank=True, null=True, verbose_name='Комментарий модератора')
    views_count = models.PositiveIntegerField(blank=True, default=0, verbose_name='Кол-во просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __repr__(self):
        return self.headline

    def __str__(self):
        return self.headline

    def is_favorite(self, user):
        return bool(FavoritesResume.objects.filter(user=user, resume=self).count())


class Experience(models.Model):
    """
    Applicant work experience
    """

    class Meta:
        get_latest_by = '-id'
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    resume = models.ForeignKey(Resume, related_name='experience', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, blank=False, verbose_name='Название компании')
    company_link = models.CharField(max_length=255, blank=True, null=True, verbose_name='Сайт компании')
    position = models.CharField(max_length=255, blank=False, verbose_name='Дожность')
    data_from = models.DateField(blank=False, verbose_name='Дата начала работы')
    data_to = models.DateField(blank=False, verbose_name='Дата окончания работы')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __repr__(self):
        return self.company_name

    def __str__(self):
        return self.company_name


class Education(models.Model):
    """
    Applicant education institutions
    """

    EDUCATION_CHOICES = (
        ('SECONDARY', 'Среднее'),
        ('SPECIAL_SECONDARY', 'Среднее специальное'),
        ('UNFINISHED_HIGHER', 'Неоконченное высшее'),
        ('HIGHER', 'Высшее'),
    )

    GRADE = (
        ('BACHELOR', 'Бакалавр'),
        ('MASTER', 'Магистр'),
        ('CANDIDATE', 'Кандидат наук'),
        ('DOCTOR', 'Доктор наук'),
    )

    class Meta:
        get_latest_by = '-id'
        verbose_name = 'Образовательное учреждение'
        verbose_name_plural = 'Образовательные учреждения'

    resume = models.ForeignKey(Resume, related_name='education', on_delete=models.CASCADE)
    education_type = models.CharField(max_length=20, blank=False, choices=EDUCATION_CHOICES,
                                      null=True, verbose_name='Тип образования')
    grade = models.CharField(max_length=20, blank=True, choices=GRADE, verbose_name='Степень')
    name = models.CharField(max_length=255, blank=False, verbose_name='Название учреждения')
    specialization = models.CharField(max_length=255, blank=False, verbose_name='Специальность')
    year_of_ending = models.PositiveIntegerField(blank=False, verbose_name='Год окончания')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class FavoritesResume(models.Model):
    """
    Favorites Resume
    """

    class Meta:
        get_latest_by = '-id'
        verbose_name = 'Избранные резюме'
        verbose_name_plural = 'Избранные резюме'
        unique_together = (("user", "resume"),)

    user = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey(to=Resume, on_delete=models.CASCADE)
