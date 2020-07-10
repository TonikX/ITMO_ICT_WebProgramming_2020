# Generated by Django 3.0 on 2020-06-13 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0002_auto_20200613_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='stewards',
        ),
        migrations.AddField(
            model_name='steward',
            name='crew',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stewards', to='airport.Crew'),
        ),
        migrations.AlterField(
            model_name='route',
            name='transit_landing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='airport.TransitLanding'),
        ),
    ]