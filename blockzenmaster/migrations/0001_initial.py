# Generated by Django 3.2.7 on 2021-09-21 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('postCode', models.CharField(blank=True, max_length=100, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryName', models.CharField(blank=True, max_length=200, null=True)),
                ('currencyCode', models.CharField(blank=True, max_length=50, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degreeName', models.CharField(blank=True, max_length=200, null=True)),
                ('remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Designations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('joiningDate', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('identityValue', models.CharField(blank=True, max_length=200, null=True)),
                ('probationPeriod', models.IntegerField(blank=True, default=0, null=True)),
                ('bloodGroup', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('mobile', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('fatherName', models.CharField(blank=True, max_length=200, null=True)),
                ('motherName', models.CharField(blank=True, max_length=200, null=True)),
                ('spouseName', models.CharField(blank=True, default='N/A', max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.CharField(blank=True, max_length=200, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.branch')),
                ('departments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.departments')),
                ('designations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.designations')),
            ],
        ),
        migrations.CreateModel(
            name='EmpOrganizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('businessType', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(blank=True, max_length=100, null=True)),
                ('groupDescription', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shiftName', models.CharField(blank=True, max_length=200, null=True)),
                ('workingHours', models.IntegerField(blank=True, default=8, null=True)),
                ('startTime', models.CharField(blank=True, max_length=50, null=True)),
                ('endTime', models.CharField(blank=True, max_length=50, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Religions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('religion', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionName', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('countries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.countries')),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveName', models.CharField(blank=True, max_length=100, null=True)),
                ('eligibility', models.CharField(blank=True, choices=[('All', 'All'), ('Male', 'Male'), ('Female', 'Female')], default='All', max_length=100, null=True)),
                ('accrualleave', models.CharField(blank=True, max_length=100, null=True)),
                ('calendar', models.CharField(blank=True, max_length=100, null=True)),
                ('encashment', models.CharField(blank=True, choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=100, null=True)),
                ('carryover', models.CharField(blank=True, choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=100, null=True)),
                ('maxLength', models.CharField(blank=True, max_length=100, null=True)),
                ('startDate', models.DateField(blank=True, default='1959-01-01', null=True)),
                ('endDate', models.DateField(blank=True, default=None, null=True)),
                ('remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastModificaitonBy', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('leavegroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blockzenmaster.leavegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('cities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.cities')),
            ],
        ),
        migrations.CreateModel(
            name='IdentityTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employmentType', models.CharField(blank=True, max_length=200, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, default=None, null=True)),
                ('jobDetails', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('cities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.cities')),
                ('employees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.emporganizations')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='employmenttype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employmenttype'),
        ),
        migrations.AddField(
            model_name='employees',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.gender'),
        ),
        migrations.AddField(
            model_name='employees',
            name='grades',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.grades'),
        ),
        migrations.AddField(
            model_name='employees',
            name='identitytypes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.identitytypes'),
        ),
        migrations.AddField(
            model_name='employees',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees'),
        ),
        migrations.AddField(
            model_name='employees',
            name='maritalstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.maritalstatus'),
        ),
        migrations.AddField(
            model_name='employees',
            name='religion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.religions'),
        ),
        migrations.AddField(
            model_name='employees',
            name='shifttype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.shifttype'),
        ),
        migrations.AddField(
            model_name='employees',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employmentstatus'),
        ),
        migrations.AddField(
            model_name='employees',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EmployeeDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentration', models.CharField(blank=True, max_length=200, null=True)),
                ('passingYear', models.IntegerField(blank=True, null=True)),
                ('sessionYear', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('resultOption', models.CharField(blank=True, choices=[('Grade', 'Grade'), ('Marks', 'Marks')], default='Grade', max_length=100, null=True)),
                ('result', models.CharField(blank=True, max_length=50, null=True)),
                ('degree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.degree')),
                ('employees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.institution')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressType', models.CharField(blank=True, choices=[('Present', 'Present'), ('Permanent', 'Permanent')], max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('postCode', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('cities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.cities')),
                ('employees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
            ],
        ),
        migrations.CreateModel(
            name='EmpEmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactName', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('relation', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('postCode', models.CharField(blank=True, default=0, max_length=100, null=True)),
                ('cities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.cities')),
                ('employees', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
            ],
        ),
        migrations.CreateModel(
            name='EmpAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, default=None, null=True)),
                ('jobDetails', models.CharField(blank=True, max_length=1000, null=True)),
                ('designations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.designations')),
                ('employees', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Divisions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisionName', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='departments',
            name='divisions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.divisions'),
        ),
        migrations.AddField(
            model_name='departments',
            name='parentDepartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.departments'),
        ),
        migrations.AddField(
            model_name='cities',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.regions'),
        ),
        migrations.AddField(
            model_name='branch',
            name='cities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.cities'),
        ),
        migrations.AddField(
            model_name='branch',
            name='createdby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='branch',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.organization'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendanceDate', models.DateField(auto_now_add=True)),
                ('checkIn', models.DateTimeField(blank=True, default=None, null=True)),
                ('checkOut', models.DateTimeField(blank=True, default=None, null=True)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('employees', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blockzenmaster.employees')),
            ],
        ),
    ]