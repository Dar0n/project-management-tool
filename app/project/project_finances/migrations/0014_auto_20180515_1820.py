# Generated by Django 2.0.3 on 2018-05-15 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_finances', '0013_remove_projectfinances_forecasts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yearlyforecast',
            old_name='forecast_further_years',
            new_name='forecast',
        ),
    ]
