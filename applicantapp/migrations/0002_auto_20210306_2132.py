# Generated by Django 3.1.7 on 2021-03-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='date_of_birth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]
