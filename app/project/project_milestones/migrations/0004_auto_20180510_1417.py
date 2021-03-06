# Generated by Django 2.0.3 on 2018-05-10 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_milestones', '0003_auto_20180510_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaryoptions',
            name='heading',
            field=models.CharField(blank=True, help_text='Kommentar Title', max_length=50, null=True, verbose_name='commentary heading'),
        ),
        migrations.AlterField(
            model_name='milestones',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_data.ProjectData', verbose_name='project name'),
        ),
    ]
