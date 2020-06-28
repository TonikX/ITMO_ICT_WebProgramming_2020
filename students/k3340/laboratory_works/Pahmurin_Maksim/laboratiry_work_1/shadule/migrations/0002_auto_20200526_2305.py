# Generated by Django 3.0.5 on 2020-05-26 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shadule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='teacher_fio',
        ),
        migrations.AlterField(
            model_name='homework',
            name='keywords',
            field=models.CharField(max_length=50, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shadule.Teacher', verbose_name='Учитель'),
        ),
    ]