# Generated by Django 3.0.6 on 2020-05-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='tc',
            field=models.IntegerField(default='1', max_length=11, verbose_name='kimlik numarası'),
            preserve_default=False,
        ),
    ]
