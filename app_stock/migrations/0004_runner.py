# Generated by Django 3.2.3 on 2023-05-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stock', '0003_stock_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('medal', models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10)),
            ],
        ),
    ]