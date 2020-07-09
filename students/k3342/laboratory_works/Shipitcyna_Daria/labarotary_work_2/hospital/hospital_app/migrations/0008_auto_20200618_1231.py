# Generated by Django 3.0.6 on 2020-06-18 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0007_auto_20200607_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='vacant',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='work_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='record',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='hospital_app.Schedule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='work_times',
            field=models.ManyToManyField(through='hospital_app.Schedule', to='hospital_app.App_times'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='app_time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='hospital_app.App_times'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(default='2000-01-01', verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('male', 'мужской'), ('female', 'женский')], max_length=6, verbose_name='Пол'),
        ),
        migrations.DeleteModel(
            name='Medical_Record',
        ),
    ]