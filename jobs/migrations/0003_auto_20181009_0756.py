# Generated by Django 2.2.dev20180919211339 on 2018-10-09 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20181009_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='user_id',
            new_name='user',
        ),
    ]
