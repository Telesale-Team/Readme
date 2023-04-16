# Generated by Django 3.2.3 on 2023-04-11 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_money', '0007_auto_20230411_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='receiptinvoice',
            name='subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_money.subject'),
        ),
    ]