# Generated by Django 3.2.3 on 2023-05-29 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_money', '0009_auto_20230411_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiptinvoice',
            old_name='created_dat',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='receiptinvoice',
            old_name='collector',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='receiptinvoice',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='receiptinvoice',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='receiptinvoice',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='receiptinvoice',
            name='image5',
        ),
    ]