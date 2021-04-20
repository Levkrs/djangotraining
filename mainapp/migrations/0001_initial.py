# Generated by Django 3.1.7 on 2021-04-10 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companyapp', '0001_initial'),
        ('applicantapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteRecrut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('0', 'На рассмотрении'), ('1', 'Принят'), ('2', 'Отклонен')], db_index=True, default='0', max_length=1, verbose_name='Статус')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicantapp.resume')),
                ('vacansy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.job')),
            ],
            options={
                'verbose_name': 'Отклик на вакансию.',
            },
        ),
        migrations.CreateModel(
            name='InviteHr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'На рассмотрении'), ('1', 'Принят'), ('2', 'Отклонен')], db_index=True, default='0', max_length=1, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.company')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicantapp.resume')),
                ('vacansy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.job')),
            ],
            options={
                'verbose_name': 'Отклик на резюме.',
            },
        ),
    ]