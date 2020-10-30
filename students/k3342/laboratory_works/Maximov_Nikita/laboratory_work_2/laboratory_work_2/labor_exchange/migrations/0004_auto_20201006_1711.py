# Generated by Django 3.0 on 2020-10-06 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labor_exchange', '0003_auto_20201006_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='employer',
        ),
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='labor_exchange.Applicant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='labor_exchange.Employer'),
            preserve_default=False,
        ),
    ]
