# Generated by Django 3.0.5 on 2020-06-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='books',
            field=models.ManyToManyField(related_name='attached_book', through='lib_app.Attachment', to='lib_app.Book', verbose_name='книги'),
        ),
    ]
