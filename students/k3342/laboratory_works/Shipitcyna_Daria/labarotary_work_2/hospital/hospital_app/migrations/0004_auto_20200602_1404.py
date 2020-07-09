# Generated by Django 3.0.6 on 2020-06-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0003_auto_20200602_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='vacant',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(verbose_name='Дата приема'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(verbose_name='Время приема'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='work_time',
            field=models.ManyToManyField(related_name='working_hours', to='hospital_app.App_times'),
        ),
    ]