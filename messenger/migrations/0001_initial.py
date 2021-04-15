# Generated by Django 3.1.7 on 2021-04-14 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companyapp', '0002_auto_20210413_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessengerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_text', models.CharField(max_length=255, verbose_name='Текст сообщения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('msg_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_from', to=settings.AUTH_USER_MODEL)),
                ('msg_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_to', to=settings.AUTH_USER_MODEL)),
                ('vacansy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacansy_message', to='companyapp.job')),
            ],
            options={
                'verbose_name': 'MSG',
            },
        ),
    ]
