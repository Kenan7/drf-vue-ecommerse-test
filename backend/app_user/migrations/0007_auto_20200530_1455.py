# Generated by Django 3.0.6 on 2020-05-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0006_auto_20200530_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon numarası'),
        ),
    ]
