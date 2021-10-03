# Generated by Django 3.2.7 on 2021-09-21 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blockzenmaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediumType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediumName', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionName', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionName', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('birthPlace', models.CharField(blank=True, max_length=200, null=True)),
                ('admissionDate', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('identityValue', models.CharField(blank=True, max_length=200, null=True)),
                ('bloodGroup', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('disability', models.BooleanField(blank=True, default=False, null=True)),
                ('disabilityDetails', models.CharField(blank=True, max_length=1000, null=True)),
                ('identificationMark', models.CharField(blank=True, max_length=200, null=True)),
                ('presentAddress', models.CharField(blank=True, max_length=1000, null=True)),
                ('presentArea', models.CharField(blank=True, max_length=200, null=True)),
                ('presentPostCode', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('permanentAddress', models.CharField(blank=True, max_length=1000, null=True)),
                ('permanentArea', models.CharField(blank=True, max_length=200, null=True)),
                ('permanentPostCode', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.gender')),
                ('grades', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.grades')),
                ('identitytypes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.identitytypes')),
                ('permanentCity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='permanent_city', to='blockzenmaster.cities')),
                ('presentCity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='present_city', to='blockzenmaster.cities')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.religions')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.studentstatus')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fatherName', models.CharField(blank=True, max_length=200, null=True)),
                ('fatherProfession', models.CharField(blank=True, max_length=200, null=True)),
                ('fatherPhone', models.CharField(blank=True, max_length=50, null=True)),
                ('fatherEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('motherName', models.CharField(blank=True, max_length=200, null=True)),
                ('motherProfession', models.CharField(blank=True, max_length=200, null=True)),
                ('motherPhone', models.CharField(blank=True, max_length=50, null=True)),
                ('motherEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('students', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.students')),
            ],
        ),
        migrations.CreateModel(
            name='LocalGuardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('profession', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('postCode', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('cities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.cities')),
                ('students', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.students')),
            ],
        ),
        migrations.CreateModel(
            name='ClassSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('classes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.classes')),
                ('mediumtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.mediumtype')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ClassDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, default=None, null=True)),
                ('createdBy', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.branch')),
                ('classTeacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
                ('classes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.classes')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.section')),
            ],
        ),
    ]
