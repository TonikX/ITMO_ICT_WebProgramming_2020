# Generated by Django 3.0.4 on 2020-05-27 23:15

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
                ('mark', models.CharField(max_length=200, verbose_name='Название марки')),
                ('c_type', models.CharField(max_length=200, verbose_name='Модель машины')),
                ('color', models.CharField(max_length=200, verbose_name='Цвет машины')),
                ('gov_num', models.IntegerField(max_length=200, verbose_name='Гос. номер')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('birth_date', models.DateTimeField(max_length=200, verbose_name='Дата Рождения')),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владельцы',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(max_length=200, verbose_name='Дата начала владения')),
                ('end_date', models.DateTimeField(max_length=200, verbose_name='Дата конца владения')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.Owner')),
            ],
            options={
                'verbose_name': 'Владение',
                'verbose_name_plural': 'Владения',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_num', models.IntegerField(max_length=200, verbose_name='Номер')),
                ('date_out', models.DateTimeField(max_length=200, verbose_name='Дата выдачи')),
                ('l_type', models.CharField(max_length=200, verbose_name='Тип лицензии')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.Owner')),
            ],
            options={
                'verbose_name': 'Удостоверение',
                'verbose_name_plural': 'Удостоверения',
            },
        ),
    ]
