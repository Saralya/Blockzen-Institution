from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from blockzenmaster.models import *

from django.contrib.admin import widgets


import datetime

## Date Picker

class DateInput(forms.DateInput):
    input_type = 'date'



######################################################################################################



class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = 'Enter Old Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(label = 'Enter New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(label = 'Re-enter New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


######################################################################################################


class DivisionForm(ModelForm):
    divisionName = forms.CharField(max_length=200, label = 'Division Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=500, label = 'Remarks', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

    class Meta:
        model = Divisions
        fields = ['divisionName', 'description']



class DepartmentForm(ModelForm):
    departmentName = forms.CharField(max_length=200, label = 'Department Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=500, label = 'Remarks', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

    class Meta:
        model = Departments
        fields = ['departmentName', 'description', 'parentDepartment', 'divisions']

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)

        self.fields['parentDepartment'].widget.attrs['class'] = 'form-control'
        self.fields['parentDepartment'].label = 'Parent Department'
        self.fields['divisions'].widget.attrs['class'] = 'form-control'
        self.fields['divisions'].label = 'Division Name'



class GradeForm(ModelForm):
    grade = forms.CharField(max_length=200, label = 'Grade', widget=forms.TextInput(attrs={'class':'form-control'}))
    remarks = forms.CharField(max_length=500, label = 'Remarks', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

    class Meta:
        model = Grades
        fields = ['grade', 'remarks']



class DesignationForm(ModelForm):
    designation = forms.CharField(max_length=200, label = 'Designation Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    remarks = forms.CharField(max_length=500, label = 'Remarks', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

    class Meta:
        model = Designations
        fields = ['designation', 'remarks']




class GenderForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Gender', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Gender
        fields = ['name']



class EmploymentStatusForm(ModelForm):
    status = forms.CharField(max_length=200, label = 'Status Title', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = EmploymentStatus
        fields = ['status', 'isActive']

    def __init__(self, *args, **kwargs):
        super(EmploymentStatusForm, self).__init__(*args, **kwargs)

        self.fields['isActive'].widget.attrs['class'] = 'form-control'
        self.fields['isActive'].label = 'Active Status'



class EmploymentTypeForm(ModelForm):
    employmentType = forms.CharField(max_length=200, label = 'Employment Type', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = EmploymentType
        fields = ['employmentType', 'isActive']

    def __init__(self, *args, **kwargs):
        super(EmploymentTypeForm, self).__init__(*args, **kwargs)

        self.fields['isActive'].widget.attrs['class'] = 'form-control'
        self.fields['isActive'].label = 'Active Status'



class IdentityTypeForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Identity Type Status', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = IdentityTypes
        fields = ['name']


class MaritalStatusForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Marital Status', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = MaritalStatus
        fields = ['name']


class DegreeForm(ModelForm):
    degreeName = forms.CharField(max_length=200, label = 'Degree', widget=forms.TextInput(attrs={'class':'form-control'}))
    remarks = forms.CharField(max_length=500, label = 'Remarks', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}), required = False)

    class Meta:
        model = Degree
        fields = ['degreeName', 'remarks']


class InstitutionForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Institution Name', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Institution
        fields = ['name', 'cities']

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)

        self.fields['cities'].widget.attrs['class'] = 'form-control'
        self.fields['cities'].label = 'City'




class EmployeeOrgForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Company Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    businessType = forms.CharField(max_length=200, label = 'Business Type', widget=forms.TextInput(attrs={'class':'form-control'}), required = False)

    class Meta:
        model = EmpOrganizations
        fields = ['name', 'businessType']

    

######################################################################################################
######################################################################################################
######################################################################################################


class EmployeeForm(ModelForm):
    empno = forms.CharField(max_length=50, label = 'Employee ID', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=200, label = 'First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, label = 'Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    birthDate = forms.DateField(widget = DateInput)
    joiningDate = forms.DateField(widget = DateInput)
    nationality = forms.CharField(max_length=200, label = 'Nationality', widget=forms.TextInput(attrs={'class':'form-control'}))
    identityValue = forms.CharField(max_length=200, label = 'Identification Number', widget=forms.TextInput(attrs={'class':'form-control'}))
    probationPeriod = forms.CharField(max_length=200, label = 'Probation Period', widget=forms.TextInput(attrs={'class':'form-control'}))
    bloodGroup = forms.CharField(max_length=10, label = 'Blood Group', widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(max_length=50, label = 'Mobile Number', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=50, label = 'Email Address', widget=forms.TextInput(attrs={'class':'form-control'}))
    fatherName = forms.CharField(max_length=200, label = "Father's Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    motherName = forms.CharField(max_length=200, label = "Mother's Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    spouseName = forms.CharField(max_length=200, label = 'Spouse Name', widget=forms.TextInput(attrs={'class':'form-control'}), required = False)

    class Meta:
        model = Employees
        fields = ['empno', 'first_name', 'last_name', 'mobile', 'email', 'gender', 'fatherName', 'motherName', 'maritalstatus', 'spouseName', 'branch', 'designations', 'departments', 'picture', 'manager', 'birthDate', 'joiningDate', 'grades', 'status', 'nationality', 'bloodGroup', 'religion', 'identitytypes', 'identityValue', 'probationPeriod', 'shifttype', 'employmenttype', 'user']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['birthDate'].widget.attrs['class'] = 'form-control'
        self.fields['joiningDate'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].label = 'Gender'
        self.fields['branch'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].label = 'Branch'
        self.fields['designations'].widget.attrs['class'] = 'form-control'
        self.fields['designations'].label = 'Designation'
        self.fields['departments'].widget.attrs['class'] = 'form-control'
        self.fields['departments'].label = 'Department'
        self.fields['manager'].widget.attrs['class'] = 'form-control'
        self.fields['manager'].label = 'Line Manager'
        self.fields['grades'].widget.attrs['class'] = 'form-control'
        self.fields['grades'].label = 'Job Grade'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].label = 'Employment Status'
        self.fields['identitytypes'].widget.attrs['class'] = 'form-control'
        self.fields['identitytypes'].label = 'Identity Type'
        self.fields['maritalstatus'].widget.attrs['class'] = 'form-control'
        self.fields['maritalstatus'].label = 'Marital Status'
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['user'].label = 'User Name'
        self.fields['religion'].widget.attrs['class'] = 'form-control'
        self.fields['religion'].label = 'Religion'
        self.fields['shifttype'].widget.attrs['class'] = 'form-control'
        self.fields['shifttype'].label = 'Shift Type'
        self.fields['employmenttype'].widget.attrs['class'] = 'form-control'
        self.fields['employmenttype'].label = 'Employment Type'





class EmployeeAddressForm(ModelForm):
    address = forms.CharField(max_length=50, label = 'Address', widget=forms.TextInput(attrs={'class':'form-control'}))
    area = forms.CharField(max_length=200, label = 'Area', widget=forms.TextInput(attrs={'class':'form-control'}))
    postCode = forms.CharField(max_length=200, label = 'Post Code', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = EmployeeAddress
        fields = ['addressType', 'address', 'area', 'cities', 'postCode']

    def __init__(self, *args, **kwargs):
        super(EmployeeAddressForm, self).__init__(*args, **kwargs)

        self.fields['addressType'].widget.attrs['class'] = 'form-control'
        self.fields['addressType'].label = 'Address Type'
        self.fields['cities'].widget.attrs['class'] = 'form-control'
        self.fields['cities'].label = 'City'



class EditEmployeeAddressForm(ModelForm):
    address = forms.CharField(max_length=50, label = 'Address', widget=forms.TextInput())
    area = forms.CharField(max_length=200, label = 'Area', widget=forms.TextInput())
    postCode = forms.CharField(max_length=200, label = 'Post Code', widget=forms.TextInput())
    

    class Meta:
        model = EmployeeAddress
        fields = ['address', 'area', 'cities', 'postCode']

    def __init__(self, *args, **kwargs):
        super(EditEmployeeAddressForm, self).__init__(*args, **kwargs)

        self.fields['cities'].label = 'City'




class EmployeeDegreeForm(ModelForm):
    concentration = forms.CharField(max_length=200, label = 'Concentration', widget=forms.TextInput(attrs={'class':'form-control'}))
    passingYear = forms.CharField(max_length=200, label = 'Passing Year', widget=forms.TextInput(attrs={'class':'form-control'}))
    sessionYear = forms.CharField(max_length=200, label = 'Session', widget=forms.TextInput(attrs={'class':'form-control'}))
    result = forms.CharField(max_length=200, label = 'Result', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = EmployeeDegree
        fields = ['degree', 'institution', 'passingYear', 'concentration', 'sessionYear', 'resultOption', 'result']

    def __init__(self, *args, **kwargs):
        super(EmployeeDegreeForm, self).__init__(*args, **kwargs)

        self.fields['degree'].widget.attrs['class'] = 'form-control'
        self.fields['degree'].label = 'Degree'
        self.fields['institution'].widget.attrs['class'] = 'form-control'
        self.fields['institution'].label = 'institution'
        self.fields['resultOption'].widget.attrs['class'] = 'form-control'
        self.fields['resultOption'].label = 'Result Type'



class EmployeeWorkForm(ModelForm):
    designation = forms.CharField(max_length=200, label = 'Designation', widget=forms.TextInput(attrs={'class':'form-control'}))
    startDate = forms.DateField(widget = DateInput)
    endDate = forms.DateField(widget = DateInput)
    jobDetails = forms.CharField(max_length=1000, label = 'Job Description', widget=forms.Textarea(attrs={'class':'form-control', 'rows':6}), required = False)
    address = forms.CharField(max_length=500, label = 'Address', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}), required = False)

    class Meta:
        model = EmploymentHistory
        fields = ['organization', 'designation', 'startDate', 'endDate', 'jobDetails', 'address', 'cities']

    def __init__(self, *args, **kwargs):
        super(EmployeeWorkForm, self).__init__(*args, **kwargs)

        self.fields['organization'].widget.attrs['class'] = 'form-control'
        self.fields['organization'].label = 'Company Name'
        self.fields['startDate'].widget.attrs['class'] = 'form-control'
        self.fields['endDate'].widget.attrs['class'] = 'form-control'
        self.fields['cities'].widget.attrs['class'] = 'form-control'
        self.fields['cities'].label = 'City'



class EmergencyContactForm(ModelForm):
    contactName = forms.CharField(max_length=200, label = 'Full Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(max_length=200, label = 'Mobile No', widget=forms.TextInput(attrs={'class':'form-control'}))
    relation = forms.CharField(max_length=200, label = 'Relation', widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=500, label = 'Address', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}), required = False)
    area = forms.CharField(max_length=200, label = 'Area', widget=forms.TextInput(attrs={'class':'form-control'}))
    postCode = forms.CharField(max_length=200, label = 'Post Code', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = EmpEmergencyContact
        fields = ['contactName', 'mobile', 'relation', 'address', 'area', 'cities', 'postCode']

    def __init__(self, *args, **kwargs):
        super(EmergencyContactForm, self).__init__(*args, **kwargs)

        self.fields['cities'].widget.attrs['class'] = 'form-control'
        self.fields['cities'].label = 'City'




class EditAttendanceForm(ModelForm):
    checkIn = forms.CharField(max_length=200, label = 'Check In', widget=forms.TextInput(attrs={'class':'form-control'}))
    checkOut = forms.CharField(max_length=200, label = 'Check Out', widget=forms.TextInput(attrs={'class':'form-control'}))
    note = forms.CharField(max_length=500, label = 'Note', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

    class Meta:
        model = Attendance
        fields = ['checkIn', 'checkOut', 'note']



class ShiftForm(ModelForm):
    shiftName = forms.CharField(max_length=200, label = 'Shift Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    workingHours = forms.CharField(max_length=200, label = 'Working Hours', widget=forms.TextInput(attrs={'class':'form-control'}))
    startTime = forms.CharField(max_length=200, label = 'Start Time', widget=forms.TextInput(attrs={'class':'form-control'}))
    endTime = forms.CharField(max_length=200, label = 'End Time', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = ShiftType
        fields = ['shiftName', 'workingHours', 'startTime', 'endTime']


class ReligionForm(ModelForm):
    religion = forms.CharField(max_length=200, label = 'Religion', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Religions
        fields = ['religion']