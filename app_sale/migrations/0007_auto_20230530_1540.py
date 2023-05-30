# Generated by Django 3.2.3 on 2023-05-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sale', '0006_auto_20230530_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='buy',
            field=models.CharField(blank=True, choices=[('ซื้อ', 'ซื้อ'), ('ยังไม่ซื้อ', 'ยังไม่ซื้อ')], default='ซื้อ', max_length=50, verbose_name='ซื้อ หรือ ไม่ซื้อ ? (เพิ่มสถานะซื้อไม่ซื้อเพื่อติดต่ออีกครั้ง)'),
        ),
    ]
