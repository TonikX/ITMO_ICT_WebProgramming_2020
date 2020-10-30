# Generated by Django 3.0 on 2020-10-06 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labor_exchange', '0008_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecertificate',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_certificates', to='labor_exchange.Applicant'),
        ),
        migrations.AlterField(
            model_name='gratuity',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gratuities', to='labor_exchange.Applicant'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professions', to='labor_exchange.Field'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='labor_exchange.Applicant'),
        ),
    ]
