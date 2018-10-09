# Generated by Django 2.2.dev20180919211339 on 2018-10-09 08:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0003_auto_20181009_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjob',
            name='closed_on',
        ),
        migrations.RemoveField(
            model_name='appliedjob',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='appliedjob',
            name='user_id',
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='create_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='job',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
