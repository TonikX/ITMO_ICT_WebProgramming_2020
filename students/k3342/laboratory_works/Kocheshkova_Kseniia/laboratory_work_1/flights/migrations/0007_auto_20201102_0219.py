# Generated by Django 3.1.2 on 2020-11-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_auto_20201102_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=150),
        ),
    ]
