# Generated by Django 3.0.6 on 2020-05-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_appuser_tc'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='province',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Şehir'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='İlçe'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='tc',
            field=models.BigIntegerField(blank=True, max_length=11, null=True, verbose_name='kimlik numarası'),
        ),
    ]
