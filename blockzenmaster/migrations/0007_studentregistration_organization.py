# Generated by Django 3.2.7 on 2021-09-23 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockzenmaster', '0006_studentregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.organization'),
        ),
    ]
