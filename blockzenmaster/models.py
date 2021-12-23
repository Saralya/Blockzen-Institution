from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from PIL import Image
import datetime

class Countries(models.Model):
    countryName = models.CharField(max_length=200, null = True, blank = True)
    currencyCode = models.CharField(max_length=50, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.countryName

class Regions(models.Model):
    regionName = models.CharField(max_length=200, null= True, blank=True)
    countries = models.ForeignKey(Countries, on_delete= models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.regionName

class Cities(models.Model):
    cityName = models.CharField(max_length=200, null= True, blank=True)
    regions = models.ForeignKey(Regions, on_delete= models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.cityName


###################################################################################################
## ORGANIZATION
###################################################################################################

class Organization(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    organization = models.ForeignKey(Organization, on_delete = models.SET_NULL, null = True, blank = True)
    address = models.CharField(max_length = 500, null = True, blank = True)
    area = models.CharField(max_length = 200, null = True, blank = True)
    cities = models.ForeignKey(Cities, on_delete = models.SET_NULL, null = True, blank = True)
    postCode = models.CharField(max_length = 100, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name


class Faculties(models.Model):
    facultyName = models.CharField(max_length=200, null= True, blank=True)
    description = models.CharField(max_length=500, null= True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.facultyName

class Departments(models.Model):
    departmentName = models.CharField(max_length=200, null= True, blank=True)
    description = models.CharField(max_length=500, null= True, blank=True)
    faculties = models.ForeignKey(Faculties, on_delete= models.SET_NULL, null = True, blank= True)
    
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.departmentName

class Grades(models.Model):
    grade = models.CharField(max_length=50, null= True, blank=True)
    remarks = models.CharField(max_length=500, null= True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.grade


class Sectors(models.Model):
    sector = models.CharField(max_length=50, null= True, blank=True)
    remarks = models.CharField(max_length=500, null= True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.sector


class Designations(models.Model):
    designation = models.CharField(max_length=200, null= True, blank=True)
    sector = models.ForeignKey(Sectors, on_delete= models.SET_NULL, null = True, blank= True)
    remarks = models.CharField(max_length=500, null= True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.designation


class Degree(models.Model):
    degreeName = models.CharField(max_length = 200, null = True, blank = True)
    remarks = models.CharField(max_length = 500, null = True, blank = True)   
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)

    def __str__(self):
        return self.degreeName

class Institution(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    cities = models.ForeignKey(Cities, on_delete= models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name


class EmploymentStatus(models.Model):
    status = models.CharField(max_length = 200, null = True, blank = True)
    isActive = models.BooleanField(default = True, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.status



class EmploymentType(models.Model):
    employmentType = models.CharField(max_length = 200, null = True, blank = True)
    isActive = models.BooleanField(default = True, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.employmentType




class IdentityTypes(models.Model):
    name = models.CharField(max_length=200, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name


class MaritalStatus(models.Model):
    name = models.CharField(max_length=200, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name



class Religions(models.Model):
    religion = models.CharField(max_length=200, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.religion

    @property
    def get_emp_count(self):
        empcount = self.employees_set.all().count()
        return empcount


class ShiftType(models.Model):
    shiftName = models.CharField(max_length=200, null = True, blank = True)
    workingHours = models.IntegerField(default = 8, null = True, blank = True)
    startTime = models.CharField(max_length=50, null = True, blank = True)
    endTime = models.CharField(max_length=50, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.shiftName


class Employees(models.Model):
    empno = models.CharField(max_length=200, null = True, blank = True)
    first_name = models.CharField(max_length=200, null = True, blank = True)
    last_name = models.CharField(max_length=200, null = True, blank = True)
    gender = models.ForeignKey(Gender, on_delete = models.SET_NULL, null = True, blank = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True, blank = True)
    
    sector = models.ForeignKey(Sectors, on_delete = models.SET_NULL, null = True, blank = True)
    designations = models.ForeignKey(Designations, on_delete = models.SET_NULL, null = True, blank = True)
    picture = models.ImageField(null= True, blank = True)
    manager = models.ForeignKey('self', on_delete= models.SET_NULL, null = True, blank = True)
    birthDate = models.DateField(null = True, blank = True)
    joiningDate = models.DateField(null = True, blank = True)
    grades = models.ForeignKey(Grades, on_delete = models.SET_NULL, null = True, blank = True)
    status = models.ForeignKey(EmploymentStatus, on_delete = models.SET_NULL, null = True, blank = True)
    nationality = models.CharField(max_length = 200, null = True, blank = True)
    identitytypes = models.ForeignKey(IdentityTypes, on_delete = models.SET_NULL, null = True, blank = True) 
    identityValue = models.CharField(max_length = 200, null = True, blank = True)
    probationPeriod = models.IntegerField(default = 0, null = True, blank = True)
    bloodGroup = models.CharField(max_length = 10, default = None, null = True, blank = True)
    mobile = models.CharField(max_length = 50, default = None, null = True, blank = True)
    email = models.CharField(max_length = 200, default = None, null = True, blank = True)
    maritalstatus = models.ForeignKey(MaritalStatus, on_delete = models.SET_NULL, null = True, blank = True)
    fatherName = models.CharField(max_length=200, null = True, blank = True)
    motherName = models.CharField(max_length=200, null = True, blank = True)
    spouseName = models.CharField(max_length=200, default = 'N/A', null = True, blank = True)
    shifttype = models.ForeignKey(ShiftType, on_delete = models.SET_NULL, null = True, blank = True)
    religion = models.ForeignKey(Religions, on_delete = models.SET_NULL, null = True, blank = True)
    employmenttype = models.ForeignKey(EmploymentType, on_delete = models.SET_NULL, null = True, blank = True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField(max_length=200, null = True, blank = True)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    @property
    def imageURL(self):
        try:
            url = self.picture.url 
        except:
            url = ''
        return url 

    @property
    def get_emp_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def get_experience(self):
        exp = datetime.date.today() - self.joiningDate
        month = exp.days // 30
        return month


    @property
    def isManager(self):
        hasTeam = False
        team = Employees.objects.filter(manager = self.id).count()
        if team > 0:
            hasTeam = True
        else:
            hasTeam = False
        return hasTeam

    





class EmployeeAddress(models.Model):
    ADDRESSTYPE_CHOICES = (
        ('Present', 'Present'),
        ('Permanent', 'Permanent'),
    )

    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null = True, blank = True)
    addressType = models.CharField(max_length=100, null=True, blank=True, choices=ADDRESSTYPE_CHOICES)
    address = models.CharField(max_length=500, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    cities = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True)
    postCode = models.CharField(default=0, max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.employees)


class EmployeeDegree(models.Model):
    RESULT_CHOICES = (
        ('Grade', 'Grade'),
        ('Marks', 'Marks'),
    )

    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null = True, blank = True)
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null = True, blank = True)
    concentration = models.CharField(max_length = 200, null = True, blank = True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null = True, blank = True)
    passingYear = models.IntegerField(null = True, blank = True)
    sessionYear = models.CharField(default = None, max_length = 200, null = True, blank = True)
    resultOption = models.CharField(default= 'Grade', max_length = 100, null = True, blank = True, choices = RESULT_CHOICES)
    result = models.CharField(max_length = 50, null = True, blank = True) 

    def __str__(self):
        return self.employees



class EmpOrganizations(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    businessType = models.CharField(max_length = 200, null = True, blank = True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class EmploymentHistory(models.Model):
    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null = True, blank = True)
    designation = models.CharField(max_length = 200, null = True, blank = True)
    organization = models.ForeignKey(EmpOrganizations, on_delete=models.SET_NULL, null = True, blank = True)
    startDate = models.DateField(null = True, blank = True)
    endDate = models.DateField(default = None, null = True, blank = True)
    jobDetails = models.CharField(max_length = 1000, null = True, blank = True)
    address = models.CharField(max_length=500, null=True, blank=True)
    cities = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.employees)


class EmpEmergencyContact(models.Model):
    employees = models.OneToOneField(Employees, on_delete=models.SET_NULL, null = True, blank = True)
    contactName = models.CharField(max_length = 200, null = True, blank = True)
    mobile = models.CharField(max_length = 50, null = True, blank = True)
    relation = models.CharField(max_length = 200, null = True, blank = True)
    address = models.CharField(max_length=500, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    cities = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True)
    postCode = models.CharField(default=0, max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.employees)



class EmpAssignment(models.Model):
    employees = models.OneToOneField(Employees, on_delete=models.SET_NULL, null = True, blank = True)
    designations = models.ForeignKey(Designations, on_delete = models.SET_NULL, null = True, blank = True)
    startDate = models.DateField(null = True, blank = True)
    endDate = models.DateField(default = None, null = True, blank = True)
    jobDetails = models.CharField(max_length = 1000, null = True, blank = True)

    def __str__(self):
        return self.employees.get_emp_name







################################################################################################
################################################################################################
## ATTENDANCE
################################################################################################
################################################################################################

class Attendance(models.Model):
    employees = models.ForeignKey(Employees, on_delete=models.SET_NULL, null = True, blank = True)
    attendanceDate = models.DateField(auto_now_add=True)
    checkIn = models.DateTimeField(default = None, null = True, blank = True) 
    checkOut = models.DateTimeField(default = None, null = True, blank = True)
    note = models.CharField(max_length = 500, null = True, blank = True)

    def __str__(self):
        return str(self.employees)


    @property
    def get_total_hour(self):
        if self.checkOut != None:
            total_hour = self.checkOut - self.checkIn
            duration = total_hour.seconds / 3600
        else:
            duration = 0
        return duration


    @property
    def get_latein(self):
        varText = ''
        time = timezone.localtime(self.checkIn).strftime("%H:%M:%S")
        if time > '10:30:00': 
            varText = 'Late'
        else:
            varText = 'OK'

        return varText





##################################################################################################
##################################################################################################
##########    LEAVE MODULE
##################################################################################################
##################################################################################################

class LeaveGroup(models.Model):
    groupName = models.CharField(max_length=100, null=True, blank=True)
    groupDescription = models.CharField(max_length=500, null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.groupName



class Leaves(models.Model):
    ELIGIBILITY_CHOICES = (
        ('All', 'All'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    LEAVE_CHOICES = (
        ('No', 'No'),
        ('Yes', 'Yes'),
    )

    leaveName = models.CharField(max_length=100, null=True, blank=True)
    leavegroup = models.ForeignKey(LeaveGroup, on_delete=models.CASCADE, null = True, blank = True)
    eligibility = models.CharField(default = 'All', max_length = 100, null = True, blank = True, choices = ELIGIBILITY_CHOICES)
    accrualleave = models.CharField(max_length=100, null=True, blank=True)
    calendar = models.CharField(max_length=100, null=True, blank=True)
    encashment = models.CharField(default = 'No', max_length = 100, null = True, blank = True, choices = LEAVE_CHOICES)
    carryover = models.CharField(default = 'No', max_length = 100, null = True, blank = True, choices = LEAVE_CHOICES)
    maxLength = models.CharField(max_length=100, null=True, blank=True)
    startDate = models.DateField(default='1959-01-01', null = True, blank = True)
    endDate = models.DateField(default = None, null = True, blank = True)
    remarks = models.CharField(max_length=500, null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    lastModified = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    lastModificaitonBy = models.CharField(default= None, max_length=50, null = True, blank = True)

    def __str__(self):
        return self.leaveName






################################################################################################
################################################################################################
## INSTITUTION MANAGEMENT
################################################################################################
################################################################################################


class StudentStatus(models.Model):
    status = models.CharField(max_length = 200, null = True, blank = True)
    isActive = models.BooleanField(default = True, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True, blank = True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.status




class Students(models.Model):
    first_name = models.CharField(max_length=200, null = True, blank = True)
    last_name = models.CharField(max_length=200, null = True, blank = True)
    gender = models.ForeignKey(Gender, on_delete = models.SET_NULL, null = True, blank = True)
    picture = models.ImageField(null= True, blank = True)
    birthDate = models.DateField(null = True, blank = True)
    birthPlace = models.CharField(max_length = 200, null = True, blank = True)
    admissionDate = models.DateField(null = True, blank = True)
    
    status = models.ForeignKey(StudentStatus, on_delete = models.SET_NULL, null = True, blank = True)
    nationality = models.CharField(max_length = 200, null = True, blank = True)
    identitytypes = models.ForeignKey(IdentityTypes, on_delete = models.SET_NULL, null = True, blank = True) 
    identityValue = models.CharField(max_length = 200, null = True, blank = True)
    bloodGroup = models.CharField(max_length = 10, default = None, null = True, blank = True)
    religion = models.ForeignKey(Religions, on_delete = models.SET_NULL, null = True, blank = True)
    disability = models.BooleanField(default = False, null = True, blank = True)
    disabilityDetails = models.CharField(max_length = 1000, null = True, blank = True)
    identificationMark = models.CharField(max_length = 200, null = True, blank = True)
    presentAddress = models.CharField(max_length = 1000, null = True, blank = True)
    presentArea = models.CharField(max_length = 200, null = True, blank = True)
    presentCity = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'present_city')
    presentPostCode = models.CharField(default=0, max_length=100, null=True, blank=True)
    permanentAddress = models.CharField(max_length = 1000, null = True, blank = True)
    permanentArea = models.CharField(max_length = 200, null = True, blank = True)
    permanentCity = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'permanent_city')
    permanentPostCode = models.CharField(default=0, max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def get_emp_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def imageURL(self):
        try:
            url = self.picture.url 
        except:
            url = ''
        return url






class Parents(models.Model):
    students = models.ForeignKey(Students, on_delete = models.SET_NULL, null = True, blank = True)
    fatherName = models.CharField(max_length=200, null= True, blank= True)
    fatherProfession = models.CharField(max_length=200, null= True, blank= True)
    fatherPhone = models.CharField(max_length=50, null= True, blank= True)
    fatherEmail = models.CharField(max_length=100, null= True, blank= True)  
    motherName = models.CharField(max_length=200, null= True, blank= True)
    motherProfession = models.CharField(max_length=200, null= True, blank= True)
    motherPhone = models.CharField(max_length=50, null= True, blank= True)
    motherEmail = models.CharField(max_length=100, null= True, blank= True)    
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)
   

    def __str__(self):
        return self.students.get_emp_name


class LocalGuardian(models.Model):
    students = models.ForeignKey(Students, on_delete = models.SET_NULL, null = True, blank = True)
    name = models.CharField(max_length=200, null= True, blank= True)
    profession = models.CharField(max_length=200, null= True, blank= True)
    phone = models.CharField(max_length=50, null= True, blank= True)
    email = models.CharField(max_length=100, null= True, blank= True)   
    address = models.CharField(max_length = 1000, null = True, blank = True)
    area = models.CharField(max_length = 200, null = True, blank = True)
    cities = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True)
    postCode = models.CharField(default=0, max_length=100, null=True, blank=True) 
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)
   

    def __str__(self):
        return self.students.get_emp_name



class Classes(models.Model):
    className = models.CharField(max_length=200, null= True, blank= True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.className


class Section(models.Model):
    
    sectionName = models.CharField(max_length=200, null= True, blank= True)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.sectionName


class Subject(models.Model):
    subjectName = models.CharField(max_length=200, null= True, blank= True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.subjectName


class Sessions(models.Model):
    sessionName = models.CharField(max_length=200, null= True, blank= True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.sessionName

class MediumType(models.Model):
    mediumName = models.CharField(max_length = 200, null = True, blank = True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.mediumName


class ClassDetail(models.Model):
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True, blank = True)
    classes = models.ForeignKey(Classes, on_delete = models.SET_NULL, null = True, blank = True)
    section = models.ForeignKey(Section, on_delete = models.SET_NULL, null = True, blank = True)
    classTeacher = models.ForeignKey(Employees, on_delete = models.SET_NULL, null = True, blank = True)
    startDate = models.DateField(null = True, blank = True)
    endDate = models.DateField(default = None, null = True, blank = True)
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    
    def __str__(self):
        return self.branch.branchName + ' - ' + self.classes.className + ' - ' + self.section.sectionName 


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Employees, on_delete = models.SET_NULL, null = True, blank = True)
    subject = models.ForeignKey(Subject, on_delete = models.SET_NULL, null = True, blank = True)
    
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.teacher.get_emp_name


class ClassSubject(models.Model):
    classes = models.ForeignKey(Classes, on_delete = models.SET_NULL, null = True, blank = True)
    subject = models.ForeignKey(Subject, on_delete = models.SET_NULL, null = True, blank = True)
    teacher = models.ForeignKey(Employees, on_delete = models.SET_NULL, null = True, blank = True)
    mediumtype = models.ForeignKey(MediumType, on_delete = models.SET_NULL, blank = True, null = True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.classes.className + ' - ' + self.subject.subjectName


class Session(models.Model):
    session = models.CharField(max_length=200, null= True, blank= True)
    month = models.CharField(max_length=200, null= True, blank= True)
    
    
    

    def __str__(self):
        return self.session




class StudentRegistration(models.Model):
    
    student = models.ForeignKey(Students, on_delete = models.SET_NULL, null = True, blank = True)
    organization = models.ForeignKey(Organization, on_delete = models.SET_NULL, null = True, blank = True)
    branch = models.ForeignKey(Branch, on_delete = models.SET_NULL, null = True, blank = True)
    classes = models.ForeignKey(Classes, on_delete = models.SET_NULL, null = True, blank = True)
    section = models.ForeignKey(Section, on_delete = models.SET_NULL, null = True, blank = True)
    roll = models.CharField(max_length=200, null= True, blank= True)
    classTeacher = models.ForeignKey(Employees, on_delete = models.SET_NULL, null = True, blank = True)
    session = models.ForeignKey(Session, on_delete = models.SET_NULL, null = True, blank = True)
    subject = models.ManyToManyField(Subject)
    
    
    createdBy = models.CharField(max_length=200, null= True, blank= True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    
    def __str__(self):
        return self.student.first_name


class StudentAttendance(models.Model):

    ATTENDANCE_CHOICES = (
    ("Present", "Present"),
    ("Absent", "Absent"),
    
    )
    student = models.ForeignKey(Students, on_delete=models.SET_NULL, null = True, blank = True)
    attendanceDate = models.DateField(auto_now_add=True)
    
    isPresent = models.CharField(max_length=200, null= True, blank= True, choices = ATTENDANCE_CHOICES)
    

    def __str__(self):
        return self.student.get_emp_name


class Exams(models.Model):
    exam = models.CharField(max_length=200, null= True, blank= True)
    description = models.CharField(max_length=200, null= True, blank= True)
    
    
    

    def __str__(self):
        return self.exam


class Terms(models.Model):
    term = models.CharField(max_length=200, null= True, blank= True)
    description = models.CharField(max_length=200, null= True, blank= True)
    
    
    

    def __str__(self):
        return self.term


class Results(models.Model):

    student = models.ForeignKey(Students, on_delete=models.SET_NULL, null = True, blank = True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null = True, blank = True)
    term = models.ForeignKey(Terms, on_delete=models.SET_NULL, null = True, blank = True)
    exam = models.ForeignKey(Exams, on_delete=models.SET_NULL, null = True, blank = True)
    mark = models.CharField(max_length=200, null= True, blank= True)

    def __str__(self):
        return self.student.get_emp_name



