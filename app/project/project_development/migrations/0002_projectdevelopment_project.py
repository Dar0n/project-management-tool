# Generated by Django 2.0.3 on 2018-05-10 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_data', '0002_auto_20180510_1319'),
        ('project_development', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdevelopment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_data.ProjectData', verbose_name='project name'),
        ),
    ]