# Generated by Django 3.2.7 on 2021-12-21 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockzenmaster', '0029_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midtermresult',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='midtermresult',
            name='student',
        ),
        migrations.RemoveField(
            model_name='midtermresult',
            name='subject',
        ),
        migrations.DeleteModel(
            name='FinaltermResult',
        ),
        migrations.DeleteModel(
            name='MidtermResult',
        ),
    ]
