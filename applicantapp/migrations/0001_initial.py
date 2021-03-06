# Generated by Django 3.1.7 on 2021-04-10 03:49

import applicantapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название учреждения')),
                ('specialization', models.CharField(max_length=255, verbose_name='Специальность')),
                ('year_of_ending', models.PositiveIntegerField(verbose_name='Год окончания')),
            ],
            options={
                'verbose_name': 'Образовательное учреждение',
                'verbose_name_plural': 'Образовательные учреждения',
                'get_latest_by': '-id',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('company_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сайт компании')),
                ('position', models.CharField(max_length=255, verbose_name='Дожность')),
                ('data_from', models.DateField(verbose_name='Дата начала работы')),
                ('data_to', models.DateField(verbose_name='Дата окончания работы')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыт работы',
                'get_latest_by': '-id',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('status', models.CharField(choices=[('0', 'Отклонено модератором'), ('1', 'Заготовка'), ('2', 'На модерации'), ('3', 'Опубликовано'), ('4', 'Черновик'), ('5', 'Скрыто'), ('9', 'Удалено')], db_index=True, default='1', max_length=1, verbose_name='Статус')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('salary', models.PositiveIntegerField(blank=True, null=True, verbose_name='Желаемая заработная плата')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('user_pic', models.ImageField(blank=True, null=True, upload_to=applicantapp.models.Resume.user_directory_path, verbose_name='Фото')),
                ('links', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на профиль в соц. сетях или сайт')),
                ('employment', models.CharField(choices=[('NO', ''), ('FT', 'Полная занятость'), ('PT', 'Частичная занятость'), ('PW', 'Проектная работа'), ('VL', 'Волонтерство'), ('WP', 'Стажировка')], max_length=20, verbose_name='Занятость')),
                ('work_schedule', models.CharField(choices=[('NO', ''), ('FD', 'Полный день'), ('SSCH', 'Сменный график'), ('FSCH', 'Гибкий график'), ('RW', 'Удаленная работа'), ('RBW', 'Вахтовый метод')], max_length=20, verbose_name='График работы')),
                ('education_type', models.CharField(choices=[('NO', ''), ('SECONDARY', 'Среднее'), ('SPECIAL_SECONDARY', 'Среднее специальное'), ('UNFINISHED_HIGHER', 'Неоконченное высшее'), ('HIGHER', 'Высшее'), ('BACHELOR', 'Бакалавр'), ('MASTER', 'Магистр'), ('CANDIDATE', 'Кандидат наук'), ('DOCTOR', 'Доктор наук')], max_length=20, verbose_name='Образование')),
                ('about_me', models.TextField(blank=True, null=True, verbose_name='Обо мне')),
                ('key_skills', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ключевые навыки')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('moder_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий модератора')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
                'get_latest_by': '-updated_at',
            },
        ),
        migrations.CreateModel(
            name='StatusResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Статус Резюме',
                'verbose_name_plural': 'Статусы Резюме',
            },
        ),
    ]
