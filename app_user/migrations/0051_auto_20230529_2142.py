# Generated by Django 3.2.3 on 2023-05-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0050_alter_profileuser_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='image',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='bank_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='หมายเลขบัญชีธนาคาร'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='image_bank',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_bank', verbose_name='สำเนาบัญชีธนาคาร'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='image_id_card',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_id_card', verbose_name='สำเนาบัตรประชาชน'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='image_profile',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='image_profile', verbose_name='รูปภาพโปรไฟล์'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ที่อยู่'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, verbose_name='เบอร์โทรศัพท์'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='worked_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='วันเริ่มงาน'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='working_experience',
            field=models.CharField(blank=True, choices=[('น้อยกว่า1', 'น้อยกว่า1'), ('1ปี', '1ปี'), ('2ปี', '2ปี'), ('มากกว่า3ปี', 'มากกว่า3ปี')], max_length=10, verbose_name='ประสบการณ์ทำงาน'),
        ),
    ]