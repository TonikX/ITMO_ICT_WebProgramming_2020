# Generated by Django 3.0.4 on 2020-04-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0009_auto_20200420_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='din',
            field=models.DateField(default='2013.12.11'),
        ),
        migrations.AddField(
            model_name='comment',
            name='dout',
            field=models.DateField(default='2013.12.12'),
        ),
    ]