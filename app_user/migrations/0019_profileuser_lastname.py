# Generated by Django 3.2.3 on 2023-04-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0018_profileuser_talen'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='lastname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
