# Generated by Django 3.1.7 on 2021-04-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicantapp', '0005_favoritesresume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='education_type',
        ),
        migrations.AddField(
            model_name='education',
            name='education_type',
            field=models.CharField(choices=[('SECONDARY', 'Среднее'), ('SPECIAL_SECONDARY', 'Среднее специальное'), ('UNFINISHED_HIGHER', 'Неоконченное высшее'), ('HIGHER', 'Высшее')], max_length=20, null=True, verbose_name='Тип образования'),
        ),
        migrations.AddField(
            model_name='education',
            name='grade',
            field=models.CharField(blank=True, choices=[('BACHELOR', 'Бакалавр'), ('MASTER', 'Магистр'), ('CANDIDATE', 'Кандидат наук'), ('DOCTOR', 'Доктор наук')], max_length=20, verbose_name='Степень'),
        ),
        migrations.AlterField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='applicantapp.resume'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='applicantapp.resume'),
        ),
    ]