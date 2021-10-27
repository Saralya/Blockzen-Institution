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


class StudentStatusForm(ModelForm):
    status = forms.CharField(max_length=200, label = 'Status', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = StudentStatus
        fields = ['status', 'isActive']

    def __init__(self, *args, **kwargs):
        super(StudentStatusForm, self).__init__(*args, **kwargs)

        self.fields['isActive'].widget.attrs['class'] = 'form-control'
        self.fields['isActive'].label = 'Active'


class StudentsForm(ModelForm):
    first_name = forms.CharField(max_length=200, label = 'First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, label = 'Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    birthPlace = forms.CharField(max_length=200, label = 'Birth Place', widget=forms.TextInput(attrs={'class':'form-control'}))
    nationality = forms.CharField(max_length=200, label = 'Nationality', widget=forms.TextInput(attrs={'class':'form-control'}))
    identityValue = forms.CharField(max_length=200, label = 'Identity Number', widget=forms.TextInput(attrs={'class':'form-control'}))
    bloodGroup = forms.CharField(max_length=200, label = 'Blood Group', widget=forms.TextInput(attrs={'class':'form-control'}))
    disabilityDetails = forms.CharField(max_length=200, label = 'Disability Details', widget=forms.TextInput(attrs={'class':'form-control'}))
    identificationMark = forms.CharField(max_length=200, label = 'Identification Mark', widget=forms.TextInput(attrs={'class':'form-control'}))
    presentAddress = forms.CharField(max_length=200, label = 'Present Address', widget=forms.TextInput(attrs={'class':'form-control'}))
    presentArea = forms.CharField(max_length=200, label = 'Present Area', widget=forms.TextInput(attrs={'class':'form-control'}))
    presentPostCode = forms.CharField(max_length=200, label = 'Present Post Code', widget=forms.TextInput(attrs={'class':'form-control'}))
    permanentAddress = forms.CharField(max_length=200, label = 'Permanent Address', widget=forms.TextInput(attrs={'class':'form-control'}))
    permanentArea = forms.CharField(max_length=200, label = 'Permanent Area', widget=forms.TextInput(attrs={'class':'form-control'}))
    permanentPostCode = forms.CharField(max_length=200, label = 'Permanent Post Code', widget=forms.TextInput(attrs={'class':'form-control'}))
    birthDate = forms.DateField(widget = DateInput)
    admissionDate = forms.DateField(widget = DateInput)
   
    

    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'gender', 'picture', 'birthDate', 'birthPlace', 'admissionDate', 'status', 'nationality', 'identitytypes', 'identityValue', 'bloodGroup', 'religion', 'disability', 'disabilityDetails', 'identificationMark', 'presentAddress', 'presentArea', 'presentCity', 'presentPostCode', 'permanentAddress', 'permanentArea', 'permanentCity', 'permanentPostCode', 'user']

    def __init__(self, *args, **kwargs):
        super(StudentsForm, self).__init__(*args, **kwargs)

        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].label = 'Gender'
        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['picture'].label = 'Picture'
        self.fields['birthDate'].widget.attrs['class'] = 'form-control'
        self.fields['birthDate'].label = 'Birth Date'
        self.fields['admissionDate'].widget.attrs['class'] = 'form-control'
        self.fields['admissionDate'].label = 'Admission Date'
        
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].label = 'Status'
        self.fields['identitytypes'].widget.attrs['class'] = 'form-control'
        self.fields['identitytypes'].label = 'Identity Type'
        self.fields['religion'].widget.attrs['class'] = 'form-control'
        self.fields['religion'].label = 'Religion'
        self.fields['disability'].widget.attrs['class'] = 'form-control'
        self.fields['disability'].label = 'Disability'
        self.fields['presentCity'].widget.attrs['class'] = 'form-control'
        self.fields['presentCity'].label = 'Present City'
        self.fields['permanentCity'].widget.attrs['class'] = 'form-control'
        self.fields['permanentCity'].label = 'Permanent City'
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['user'].label = 'User'


class ParentsForm(ModelForm):
    fatherName = forms.CharField(max_length=200, label = 'Father Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    fatherProfession = forms.CharField(max_length=200, label = 'Father Profession', widget=forms.TextInput(attrs={'class':'form-control'}))
    fatherPhone = forms.CharField(max_length=200, label = 'Father Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
    fatherEmail = forms.CharField(max_length=200, label = 'Father Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    motherName = forms.CharField(max_length=200, label = 'Mother Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    motherProfession = forms.CharField(max_length=200, label = 'Mother Profession', widget=forms.TextInput(attrs={'class':'form-control'}))
    motherPhone = forms.CharField(max_length=200, label = 'Mother Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
    motherEmail = forms.CharField(max_length=200, label = 'Mother Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = Parents
        fields = ['students', 'fatherName', 'fatherProfession', 'fatherPhone', 'fatherEmail', 'motherName', 'motherProfession', 'motherPhone', 'motherEmail']

    def __init__(self, *args, **kwargs):
        super(ParentsForm, self).__init__(*args, **kwargs)

        self.fields['students'].widget.attrs['class'] = 'form-control'
        self.fields['students'].label = 'Student'


class LocalGuardianForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    profession = forms.CharField(max_length=200, label = 'Profession', widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=200, label = 'Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=200, label = 'Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=200, label = 'Address', widget=forms.TextInput(attrs={'class':'form-control'}))
    area = forms.CharField(max_length=200, label = 'Area', widget=forms.TextInput(attrs={'class':'form-control'}))
    postCode = forms.CharField(max_length=200, label = 'Post Code', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    

    class Meta:
        model = LocalGuardian
        fields = ['students', 'name', 'profession', 'phone', 'email', 'address', 'area', 'cities', 'postCode']

    def __init__(self, *args, **kwargs):
        super(LocalGuardianForm, self).__init__(*args, **kwargs)

        self.fields['students'].widget.attrs['class'] = 'form-control'
        self.fields['students'].label = 'Student'
        self.fields['cities'].widget.attrs['class'] = 'form-control'
        self.fields['cities'].label = 'City'


class ClassesForm(ModelForm):
    className = forms.CharField(max_length=200, label = 'Class Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, label = 'Description', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = Classes
        fields = ['className', 'branch', 'description']

    def __init__(self, *args, **kwargs):
        super(ClassesForm, self).__init__(*args, **kwargs)

        self.fields['branch'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].label = 'Branch'


class SectionForm(ModelForm):
    sectionName = forms.CharField(max_length=200, label = 'Section Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, label = 'Description', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = Section
        fields = [ 'sectionName', 'classes', 'description']

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)

        self.fields['classes'].widget.attrs['class'] = 'form-control'
        self.fields['classes'].label = 'Class'

    


class SubjectForm(ModelForm):
    subjectName = forms.CharField(max_length=200, label = 'Subject Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, label = 'Description', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = Subject
        fields = ['subjectName', 'description']


class SessionsForm(ModelForm):
    sessionName = forms.CharField(max_length=200, label = 'Session Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, label = 'Description', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = Sessions
        fields = ['sessionName', 'description']


class MediumTypeForm(ModelForm):
    mediumName = forms.CharField(max_length=200, label = 'Medium Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, label = 'Description', widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = MediumType
        fields = ['mediumName', 'description']


class ClassDetailForm(ModelForm):
    
    startDate = forms.DateField(widget = DateInput)
    endDate = forms.DateField(widget = DateInput)
    

    class Meta:
        model = ClassDetail
        fields = ['branch', 'classes', 'section', 'classTeacher', 'startDate', 'endDate']

    def __init__(self, *args, **kwargs):
        super(ClassDetailForm, self).__init__(*args, **kwargs)

        self.fields['branch'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].label = 'Branch'
        self.fields['classes'].widget.attrs['class'] = 'form-control'
        self.fields['classes'].label = 'Class'
        self.fields['section'].widget.attrs['class'] = 'form-control'
        self.fields['section'].label = 'Section'
        self.fields['classTeacher'].widget.attrs['class'] = 'form-control'
        self.fields['classTeacher'].label = 'Class Teacher'
        self.fields['startDate'].widget.attrs['class'] = 'form-control'
        self.fields['startDate'].label = 'Start Date'
        self.fields['endDate'].widget.attrs['class'] = 'form-control'
        self.fields['endDate'].label = 'End Date'


class StudentRegistrationForm(ModelForm):
    
   
    

    class Meta:
        model = StudentRegistration
        fields = ['student','organization','branch', 'classes', 'section', 'roll', 'classTeacher', 'session']

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['student'].widget.attrs['class'] = 'form-control'
        self.fields['student'].label = 'Student'
        self.fields['organization'].widget.attrs['class'] = 'form-control'
        self.fields['organization'].label = 'Organization'
        self.fields['branch'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].label = 'Branch'
        self.fields['classes'].widget.attrs['class'] = 'form-control'
        self.fields['classes'].label = 'Class'
        self.fields['section'].widget.attrs['class'] = 'form-control'
        self.fields['section'].label = 'Section'
        self.fields['roll'].widget.attrs['class'] = 'form-control'
        self.fields['roll'].label = 'Roll No'
        self.fields['classTeacher'].widget.attrs['class'] = 'form-control'
        self.fields['classTeacher'].label = 'Class Teacher'
        self.fields['session'].widget.attrs['class'] = 'form-control'
        self.fields['session'].label = 'Session'
        


class ClassSubjectForm(ModelForm):
    
    
    description = forms.CharField(max_length=200, label = 'Description', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)

    class Meta:
        model = ClassSubject
        fields = ['classes', 'subject', 'teacher', 'mediumtype', 'description']

    def __init__(self, *args, **kwargs):
        super(ClassSubjectForm, self).__init__(*args, **kwargs)

        self.fields['classes'].widget.attrs['class'] = 'form-control'
        self.fields['classes'].label = 'Class'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].label = 'Subject'
        self.fields['teacher'].widget.attrs['class'] = 'form-control'
        self.fields['teacher'].label = 'Teacher'
        self.fields['mediumtype'].widget.attrs['class'] = 'form-control'
        self.fields['mediumtype'].label = 'Medium Type'


class TeacherSubjectForm(ModelForm):
    
    
    

    class Meta:
        model = TeacherSubject
        fields = ['teacher', 'subject']

    def __init__(self, *args, **kwargs):
        super(TeacherSubjectForm, self).__init__(*args, **kwargs)

        self.fields['teacher'].widget.attrs['class'] = 'form-control'
        self.fields['teacher'].label = 'Teacher'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].label = 'Preferred Subject'


class SessionForm(ModelForm):
    
    
    session = forms.CharField(max_length=200, label = 'Session', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    month = forms.CharField(max_length=200, label = 'Month', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)

    class Meta:
        model = Session
        fields = ['session', 'month']


        
        

    