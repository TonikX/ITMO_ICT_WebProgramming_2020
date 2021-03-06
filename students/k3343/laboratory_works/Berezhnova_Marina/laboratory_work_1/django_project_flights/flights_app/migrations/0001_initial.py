# Generated by Django 3.0.4 on 2020-04-17 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTypeDefs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(choices=[(0, 'arrival'), (1, 'departure')], default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights_app.Companies')),
                ('gate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights_app.Gates')),
            ],
        ),
        migrations.CreateModel(
            name='FlightActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights_app.Flights')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights_app.ActivityTypeDefs')),
            ],
        ),
    ]
