# Generated by Django 3.0.8 on 2020-07-02 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_tours_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='second',
            new_name='second_date',
        ),
    ]