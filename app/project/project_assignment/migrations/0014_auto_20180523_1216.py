# Generated by Django 2.0.3 on 2018-05-23 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_assignment', '0013_auto_20180522_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectassignment',
            name='project',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_assignment', to='project_data.ProjectData', verbose_name='project name'),
        ),
    ]
