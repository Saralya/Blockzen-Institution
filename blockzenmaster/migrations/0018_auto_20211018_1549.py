# Generated by Django 3.2.7 on 2021-10-18 09:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blockzenmaster', '0017_remove_studentregistration_attendance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Divisions',
            new_name='Faculties',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='divisions',
            new_name='faculties',
        ),
        migrations.RenameField(
            model_name='faculties',
            old_name='divisionName',
            new_name='facultyName',
        ),
        migrations.RemoveField(
            model_name='departments',
            name='parentDepartment',
        ),
    ]
