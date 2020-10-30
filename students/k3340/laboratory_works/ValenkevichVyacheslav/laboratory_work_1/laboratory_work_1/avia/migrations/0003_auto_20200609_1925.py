# Generated by Django 3.0 on 2020-06-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avia', '0002_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_type',
            field=models.CharField(blank=True, choices=[('Информация_о_задержке', 'Информация О Задержке'), ('Изменение_номера_выхода', 'Изменение Номера Выхода'), ('Иное', 'Иное')], max_length=50, verbose_name='Тип комментария'),
        ),
    ]
