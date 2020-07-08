# Generated by Django 3.0.7 on 2020-07-01 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('middle_name', models.TextField(verbose_name='Отчество')),
                ('specialty', models.TextField(verbose_name='Специальность')),
                ('education', models.TextField(verbose_name='Образование')),
                ('sex', models.CharField(choices=[('М', 'Man'), ('Ж', 'Woman')], default='М', max_length=1, verbose_name='Пол')),
                ('bdate', models.DateField()),
                ('start_contract', models.DateField()),
                ('end_contract', models.DateField()),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Доктора',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('price', models.TextField(max_length=100, verbose_name='Цена')),
                ('paid', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Doctor', verbose_name='Доктор')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Patient', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
        migrations.CreateModel(
            name='Scheduleofdoctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=True)),
                ('tuesday', models.BooleanField(default=True)),
                ('wednesday', models.BooleanField(default=True)),
                ('thursday', models.BooleanField(default=True)),
                ('friday', models.BooleanField(default=True)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('operating_time', models.TextField(verbose_name='Время работы')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Doctor', verbose_name='доктор')),
            ],
            options={
                'verbose_name': 'Раписание',
                'verbose_name_plural': 'Раписание',
            },
        ),
        migrations.CreateModel(
            name='Medicalrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseases', models.TextField(verbose_name='Заболевания')),
                ('date_of_acceptance', models.DateField(verbose_name='Дата принятия')),
                ('diagnosis', models.TextField(verbose_name='Диагноз')),
                ('current_state', models.TextField(verbose_name='Заболевания')),
                ('recommendations_for_treatment', models.TextField(verbose_name='Рекомендации по лечению')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Patient', verbose_name='пациент')),
            ],
            options={
                'verbose_name': 'Мед. Карта',
                'verbose_name_plural': 'Мед. Карты',
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet_number', models.CharField(max_length=3, verbose_name='Номер кабинета')),
                ('operating_time', models.TextField(verbose_name='Время работы')),
                ('telephone', models.CharField(max_length=11, verbose_name='Телефона')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Doctor', verbose_name='Ответственный')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
    ]
