# Generated by Django 4.2 on 2023-09-09 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]