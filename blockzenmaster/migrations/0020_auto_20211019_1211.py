# Generated by Django 3.2.7 on 2021-10-19 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockzenmaster', '0019_auto_20211018_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='departments',
        ),
        migrations.AddField(
            model_name='employees',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.sectors'),
        ),
    ]
