# Generated by Django 2.0.3 on 2018-05-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_finances', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfinances',
            name='project',
            field=models.ForeignKey(on_delete='models.SET_NULL', to='project_data.ProjectData', verbose_name='project name'),
        ),
    ]
