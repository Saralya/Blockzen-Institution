# Generated by Django 3.2.7 on 2021-09-29 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockzenmaster', '0016_alter_studentregistration_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentregistration',
            name='attendance',
        ),
    ]
