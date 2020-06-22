# Generated by Django 3.0.5 on 2020-04-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0008_auto_20200415_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='type',
            field=models.CharField(choices=[('T1', 'Оплата'), ('T2', 'Дресс-код'), ('T3', 'Уровень подготовки'), ('T4', 'Другое')], default='Оплата', max_length=20, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='level',
            field=models.CharField(choices=[('Начинающи', 'Начинающий'), ('Продвинутый', 'Продвинутый'), ('Любой', 'Любой')], max_length=20, verbose_name='Уроовень подготовки'),
        ),
    ]