# Generated by Django 3.2 on 2023-04-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_auto_20230402_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='age',
            field=models.IntegerField(blank=True, default=1001),
        ),
    ]