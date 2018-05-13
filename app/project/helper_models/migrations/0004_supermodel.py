# Generated by Django 2.0.3 on 2018-05-13 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_data', '0004_auto_20180511_2025'),
        ('helper_models', '0003_auto_20180511_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_data.ProjectData')),
            ],
        ),
    ]
