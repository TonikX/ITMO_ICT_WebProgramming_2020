# Generated by Django 3.0.4 on 2020-03-11 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('second_name', models.CharField(max_length=128)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('color', models.CharField(max_length=128)),
                ('vehicle_number', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Person')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')], default=1)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Person')),
            ],
        ),
    ]
