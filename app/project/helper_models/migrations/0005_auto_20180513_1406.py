# Generated by Django 2.0.3 on 2018-05-13 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helper_models', '0004_supermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supermodel',
            name='project_data',
        ),
        migrations.DeleteModel(
            name='SuperModel',
        ),
    ]
