# Generated by Django 3.2.3 on 2023-05-01 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0024_remove_profileuser_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('team', models.ImageField(blank=True, default='default.png', null=True, upload_to='image_teams')),
                ('detail', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_user.positions'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_user.team'),
        ),
    ]