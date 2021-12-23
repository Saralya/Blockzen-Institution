# Generated by Django 3.2.7 on 2021-12-23 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockzenmaster', '0030_auto_20211221_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(blank=True, max_length=200, null=True)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.exams')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.students')),
                ('term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.terms')),
            ],
        ),
    ]
