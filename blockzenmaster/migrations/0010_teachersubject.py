# Generated by Django 3.2.7 on 2021-09-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockzenmaster', '0009_auto_20210926_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.subject')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
            ],
        ),
    ]