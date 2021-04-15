# Generated by Django 3.1.7 on 2021-04-14 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicantapp', '0004_auto_20210413_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoritesResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicantapp.resume')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Избранные резюме',
                'verbose_name_plural': 'Избранные резюме',
                'get_latest_by': '-id',
                'unique_together': {('user', 'resume')},
            },
        ),
    ]
