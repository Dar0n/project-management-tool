# Generated by Django 2.0.3 on 2018-05-23 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_dependencies', '0007_auto_20180516_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdependencies',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_dependencies', to='project_data.ProjectData', verbose_name='project name'),
        ),
    ]
