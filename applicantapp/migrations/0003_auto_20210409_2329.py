# Generated by Django 3.1.7 on 2021-04-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantapp', '0002_auto_20210409_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education_type',
            field=models.CharField(choices=[('NO', ''), ('SECONDARY', 'Среднее'), ('SPECIAL_SECONDARY', 'Среднее специальное'), ('UNFINISHED_HIGHER', 'Неоконченное высшее'), ('HIGHER', 'Высшее'), ('BACHELOR', 'Бакалавр'), ('MASTER', 'Магистр'), ('CANDIDATE', 'Кандидат наук'), ('DOCTOR', 'Доктор наук')], max_length=20, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='employment',
            field=models.CharField(choices=[('NO', ''), ('FT', 'Полная занятость'), ('PT', 'Частичная занятость'), ('PW', 'Проектная работа'), ('VL', 'Волонтерство'), ('WP', 'Стажировка')], max_length=20, verbose_name='Занятость'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='work_schedule',
            field=models.CharField(choices=[('NO', ''), ('FD', 'Полный день'), ('SSCH', 'Сменный график'), ('FSCH', 'Гибкий график'), ('RW', 'Удаленная работа'), ('RBW', 'Вахтовый метод')], max_length=20, verbose_name='График работы'),
        ),
    ]
