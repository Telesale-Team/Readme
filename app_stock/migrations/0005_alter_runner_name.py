# Generated by Django 3.2.3 on 2023-05-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0004_runner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='name',
            field=models.CharField(max_length=60, verbose_name="person's first name"),
        ),
    ]