# Generated by Django 3.0.6 on 2020-05-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_auto_20200520_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='tc',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='kimlik numarası'),
        ),
    ]
