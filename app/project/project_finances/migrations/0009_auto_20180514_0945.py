# Generated by Django 2.0.3 on 2018-05-14 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_finances', '0008_auto_20180514_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfinances',
            name='project',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_finances', to='project_data.ProjectData', verbose_name='project name'),
        ),
        migrations.AlterField(
            model_name='yearlyforecast',
            name='project_finance',
            field=models.ForeignKey(help_text='Prognosen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='yearly_forecasts', to='project_finances.ProjectFinances', verbose_name='project finance'),
        ),
    ]
