# Generated by Django 2.0.3 on 2018-05-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_development', '0002_projectdevelopment_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstatusdropdown',
            name='value',
            field=models.CharField(max_length=20, null=True, verbose_name='status value'),
        ),
        migrations.AlterField(
            model_name='projecttendencydropdown',
            name='value',
            field=models.CharField(max_length=20, null=True, verbose_name='tendency value'),
        ),
    ]
