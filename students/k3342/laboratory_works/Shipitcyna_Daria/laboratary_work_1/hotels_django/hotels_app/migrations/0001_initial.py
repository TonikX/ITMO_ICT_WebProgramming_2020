# Generated by Django 3.0.5 on 2020-04-18 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Удобство',
                'verbose_name_plural': 'Удобства',
            },
        ),
        migrations.CreateModel(
            name='Room_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип комнаты',
                'verbose_name_plural': 'Типы комнат',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название отеля')),
                ('description', models.CharField(max_length=50, verbose_name='Описание')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('capacity', models.IntegerField(verbose_name='Вместимость')),
                ('owner', models.CharField(max_length=50, verbose_name='Владелец')),
                ('facilities', models.ManyToManyField(to='hotels_app.Facilities')),
                ('room_types', models.ManyToManyField(to='hotels_app.Room_types')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('start_living', models.DateField(verbose_name='Дата начала проживания')),
                ('end_living', models.DateField(verbose_name='Дата окончания проживания')),
                ('rating', models.CharField(choices=[('1', 'УЖАСНО'), ('2', 'ОЧЕНЬ ПЛОХО'), ('3', 'ПЛОХО'), ('4', 'УДОВЛИТВОРИТЕЛЬНО'), ('5', 'СРЕДНЕ'), ('6', 'ВЫШЕ СРЕДНЕГО'), ('7', 'ХОРОШО'), ('8', 'ОЧЕНЬ ХОРОШО'), ('9', 'ОТЛИЧНО'), ('10', 'ПРЕВОСХОДНО')], max_length=2, verbose_name='Рейтинг')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels_app.Hotel', verbose_name='Отель')),
            ],
        ),
    ]
