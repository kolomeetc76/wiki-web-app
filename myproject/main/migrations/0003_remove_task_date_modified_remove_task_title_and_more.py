# Generated by Django 4.2.6 on 2023-10-18 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_date_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='title_post',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
