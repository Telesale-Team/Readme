# Generated by Django 3.2.3 on 2023-04-18 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0019_profileuser_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileuser',
            old_name='details',
            new_name='worked',
        ),
    ]
