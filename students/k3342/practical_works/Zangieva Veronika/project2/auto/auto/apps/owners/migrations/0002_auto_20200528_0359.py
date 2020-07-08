# Generated by Django 3.0.4 on 2020-05-28 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownership',
            name='owner',
        ),
        migrations.AddField(
            model_name='ownership',
            name='owners',
            field=models.ManyToManyField(to='owners.Owner'),
        ),
    ]
