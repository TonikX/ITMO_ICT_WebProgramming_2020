# Generated by Django 3.0.5 on 2020-04-19 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Механик'), (2, 'Пилот')], default=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raceapp.Team', verbose_name='Команда'),
        ),
    ]