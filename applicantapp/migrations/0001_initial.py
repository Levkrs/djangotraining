# Generated by Django 3.1.7 on 2021-03-06 18:31

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
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('salary', models.PositiveIntegerField(null=True, verbose_name='Желаемая заработная плата')),
                ('date_of_birth', models.DateTimeField(verbose_name='Дата рождения')),
                ('is_active', models.BooleanField(default=False, verbose_name='Резюме активно')),
                ('is_cheked', models.BooleanField(default=False, verbose_name='Резюме проверенно модератором')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('user_pic', models.ImageField(height_field=200, upload_to='media/photo', verbose_name='Фото', width_field=200)),
                ('links', models.CharField(max_length=255, null=True, verbose_name='Ссылка на профиль в соц. сетях или сайт')),
                ('employment', models.CharField(choices=[('FT', 'Полная занятость'), ('PT', 'Частичная занятость'), ('PW', 'Проектная работа'), ('VL', 'Волонтерство'), ('WP', 'Стажировка')], default='FT', max_length=20, verbose_name='Занятость')),
                ('work_schedule', models.CharField(choices=[('FD', 'Полный день'), ('SSCH', 'Сменный график'), ('FSCH', 'Гибкий график'), ('RW', 'Удаленная работа'), ('RBW', 'Вахтовый метод')], default='FD', max_length=20, verbose_name='График работы')),
                ('education', models.CharField(choices=[('SECONDARY', 'Среднее'), ('SPECIAL_SECONDARY', 'Среднее специальное'), ('UNFINISHED_HIGHER', 'Неоконченное высшее'), ('HIGHER', 'Высшее'), ('BACHELOR', 'Бакалавр'), ('MASTER', 'Магистр'), ('CANDIDATE', 'Кандидат наук'), ('DOCTOR', 'Доктор наук')], default='HIGHER', max_length=20, verbose_name='Образование')),
                ('about_me', models.TextField(null=True, verbose_name='Обо мне')),
                ('key_skills', models.CharField(max_length=255, null=True, verbose_name='Ключевые навыки')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('moder_comment', models.TextField(null=True, verbose_name='Комментарий модератора')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
                'get_latest_by': '-updated_at',
            },
        ),
    ]