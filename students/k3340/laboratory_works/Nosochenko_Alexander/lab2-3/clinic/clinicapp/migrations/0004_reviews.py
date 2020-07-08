# Generated by Django 3.0.7 on 2020-07-08 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicapp', '0003_reception'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=100, verbose_name='Отзыв')),
                ('reception', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicapp.Reception', verbose_name='Запись')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
