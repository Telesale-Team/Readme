# Generated by Django 3.2.3 on 2023-05-01 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0023_auto_20230501_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='user_id',
        ),
    ]
