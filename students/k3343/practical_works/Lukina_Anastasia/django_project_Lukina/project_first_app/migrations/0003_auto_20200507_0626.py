# Generated by Django 2.1.5 on 2020-05-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20200507_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='birth_date',
            field=models.DateField(default='2000-00-00'),
        ),
    ]
