# Generated by Django 3.2.3 on 2023-05-29 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='อายุ')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ความสนใจของลูกค้า')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ที่มาของลูกค้า')),
            ],
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='เว็บไซต์ทำการตลาด')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ชื่อลูกค้า')),
                ('buy', models.CharField(blank=True, choices=[('ซื้อ', 'ซื้อ'), ('ยังไม่ซื้อ', 'ยังไม่ซื้อ')], max_length=10, verbose_name='อายุโดยประมาณ')),
                ('sex', models.CharField(blank=True, choices=[('ชาย', 'ชาย'), ('หญิง', 'หญิง')], max_length=10, verbose_name='อายุโดยประมาณ')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sale.age')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sale.interest')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sale.source')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('web', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sale.web')),
            ],
            options={
                'verbose_name': 'name',
                'verbose_name_plural': 'Sale',
                'ordering': ['id'],
            },
        ),
    ]
