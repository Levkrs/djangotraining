# Generated by Django 3.1.7 on 2021-04-09 06:39

import companyapp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Наименование компании')),
                ('status', models.CharField(choices=[('0', 'Отклонена модератором'), ('1', 'Заготовка'), ('2', 'На модерации'), ('3', 'Опубликована'), ('4', 'Черновик'), ('9', 'Удалена')], db_index=True, default='1', max_length=1, verbose_name='Статус')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=companyapp.models.Company.user_directory_path, verbose_name='Логотип')),
                ('headline', models.CharField(blank=True, max_length=255, verbose_name='Слоган')),
                ('short_description', models.CharField(max_length=255, verbose_name='Краткое описание')),
                ('detail', models.TextField(blank=True, verbose_name='Подробное описание')),
                ('location', models.CharField(db_index=True, max_length=255, verbose_name='Местонахождение')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на сайт / соц.сеть')),
                ('moder_comment', models.TextField(default='Комментарий: ', verbose_name='Заключение модератора')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Число просмотров')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='company', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Отклонена модератором'), ('1', 'Заготовка'), ('2', 'На модерации'), ('3', 'Опубликована'), ('4', 'Черновик'), ('5', 'Скрыта'), ('6', 'Закрыта'), ('9', 'Удалена')], db_index=True, default='1', max_length=1, verbose_name='Статус')),
                ('grade', models.CharField(choices=[('NO', ''), ('TR', 'Trainee'), ('JR', 'Junior'), ('MD', 'Middle'), ('SR', 'Senior'), ('TL', 'TeamLead'), ('TD', 'CTO')], db_index=True, default='NO', max_length=2, verbose_name='Классность')),
                ('category', models.CharField(choices=[('NO', ''), ('FLS', 'Full Stack'), ('FED', 'Front-end'), ('BED', 'Back-end'), ('SW', 'Software'), ('AI', 'AI & ML'), ('BD', 'Big Data'), ('AND', 'Android'), ('IOS', 'iOS'), ('IOT', 'IoT'), ('QA', 'QA Engineer'), ('GD', 'GameDev'), ('PJM', 'Project Manager'), ('PDM', 'Product Manager')], db_index=True, default='NO', max_length=3, verbose_name='Категория')),
                ('salary', models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='Зарплата')),
                ('city', models.CharField(db_index=True, max_length=255, verbose_name='Город')),
                ('employment', models.CharField(choices=[('FT', 'Полная занятость'), ('PT', 'Частичная занятость'), ('PW', 'Проектная работа'), ('VL', 'Волонтерство'), ('WP', 'Стажировка')], db_index=True, default='FT', max_length=2, verbose_name='Тип занятости')),
                ('work_schedule', models.CharField(choices=[('FD', 'Полный день'), ('SSCH', 'Сменный график'), ('FSCH', 'Гибкий график'), ('RW', 'Удаленная работа'), ('RBW', 'Вахтовый метод')], db_index=True, default='FD', max_length=4, verbose_name='График работы')),
                ('experience', models.CharField(choices=[('WE', 'Без опыта'), ('SM', 'До 1 года'), ('MD', '1-3 года'), ('BG', 'Более 3 лет')], db_index=True, default='WE', max_length=2, verbose_name='Опыт работы')),
                ('short_description', models.CharField(max_length=255, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Подробное описание')),
                ('skills', models.CharField(blank=True, max_length=255, verbose_name='Навыки')),
                ('moder_comment', models.TextField(default='Комментарий: ', verbose_name='Заключение модератора')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Число просмотров')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='companyapp.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ('status', '-created_at'),
            },
        ),
    ]
