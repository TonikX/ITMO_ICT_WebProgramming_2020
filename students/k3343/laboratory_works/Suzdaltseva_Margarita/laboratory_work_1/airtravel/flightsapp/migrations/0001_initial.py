# Generated by Django 3.0.5 on 2020-04-17 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Авиакомпания',
                'verbose_name_plural': 'Авиакомпании',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Гейт',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightnum', models.CharField(max_length=7)),
                ('flighttype', models.CharField(choices=[('D', 'departure'), ('A', 'arrival')], max_length=1)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightsapp.Company')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightsapp.Direction')),
                ('gate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flightsapp.Gate')),
            ],
            options={
                'verbose_name': 'Авиа перелёт',
                'verbose_name_plural': 'Авиа перелёты',
            },
        ),
    ]
