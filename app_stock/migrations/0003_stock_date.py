# Generated by Django 3.2.3 on 2023-05-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0002_auto_20230502_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]