# Generated by Django 3.1.7 on 2021-03-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantapp', '0005_auto_20210306_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user_pic',
            field=models.ImageField(blank=True, null=True, upload_to='resume/photo', verbose_name='Фото'),
        ),
    ]