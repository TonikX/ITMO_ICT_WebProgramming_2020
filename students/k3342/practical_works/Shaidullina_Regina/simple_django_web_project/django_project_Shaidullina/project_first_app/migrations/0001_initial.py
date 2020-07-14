# Generated by Django 3.0.4 on 2020-03-21 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('colour', models.CharField(max_length=30)),
                ('car_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start_own', models.DateField()),
                ('date_end_own', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='DriversLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=30)),
                ('date_issue', models.DateField()),
                ('type', models.CharField(max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='members',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Owner'),
        ),
    ]