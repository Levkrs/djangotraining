# Generated by Django 3.1.7 on 2021-04-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantapp', '0003_auto_20210413_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='views_count',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Кол-во просмотров'),
        ),
    ]
