# Generated by Django 3.2.7 on 2021-09-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockzenmaster', '0007_studentregistration_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='roll',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
