# Generated by Django 3.1.7 on 2021-03-13 15:38

import applicantapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantapp', '0006_auto_20210313_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user_pic',
            field=models.ImageField(blank=True, null=True, upload_to=applicantapp.models.Resume.user_directory_path, verbose_name='Фото'),
        ),
    ]