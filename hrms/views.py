from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hrms.forms import *
from blockzenmaster.models import *
from blockzenmaster.decorators import admin_only




def changepassword(request):
    base = 'adminpanel/adminbase.html'
    header_text = 'Change Password'

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password changed successfully.')
            return redirect('home')
        
    else:
        form = ChangePasswordForm(request.user)

    context = {
        'form' : form,
        'base' : base,
        'header_text' : header_text,
    }  
    return render(request, 'blockzenmaster/entry.html', context)




## Faculty
@admin_only
def viewfaculties(request):
    headerText = 'Faculties'
    createData = 'createfaculties'
    faculties = Faculties.objects.all()

    context  = {
        'faculties' : faculties,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



def createfaculties(request):
    headerText = 'Divisions'
    form = FacultiesForm()

    if request.method == 'POST':
        form = FacultiesForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewfaculties') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def editfaculties(request, varCode):
    headerText = 'Faculties'
    faculties = Faculties.objects.get(id = varCode)
    form = FacultiesForm(instance = faculties)

    if request.method == 'POST':
        form = FacultiesForm(request.POST, instance = faculties)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewfaculties')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def deletefaculties(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Faculties'
    returnUrl = 'viewfaculties'

    deletedVal = Faculties.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewfaculties')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.facultyName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)



## Department
@admin_only
def viewdepartments(request):
    headerText = 'Departments'
    createData = 'createdepartment'
    department = Departments.objects.all()

    context  = {
        'department' : department,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def createdepartment(request):
    headerText = 'Department'
    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewdepartments') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editdepartment(request, varCode):
    headerText = 'Department'
    department = Departments.objects.get(id = varCode)
    form = DepartmentForm(instance = department)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance = department)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewdepartments')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deletedepartment(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Department'
    returnUrl = 'viewdepartments'

    deletedVal = Departments.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewdepartments')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.departmentName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)



## Grades
@admin_only
def viewgrades(request):
    headerText = 'Grades'
    createData = 'creategrade'
    grades = Grades.objects.all()

    context  = {
        'grades' : grades,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def creategrade(request):
    headerText = 'Grades'
    form = GradeForm()

    if request.method == 'POST':
        form = GradeForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewgrades') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editgrade(request, varCode):
    headerText = 'Grades'
    grade = Grades.objects.get(id = varCode)
    form = GradeForm(instance = grade)

    if request.method == 'POST':
        form = GradeForm(request.POST, instance = grade)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewgrades')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deletegrade(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Grade'
    returnUrl = 'viewgrades'

    deletedVal = Grades.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewgrades')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.grade,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def viewsector(request):
    headerText = 'Sectors'
    createData = 'createsector'
    sector = Sectors.objects.all()

    context  = {
        'sector' : sector,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createsector(request):
    headerText = 'Sectors'
    form = SectorsForm()

    if request.method == 'POST':
        form = SectorsForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewsector') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editsector(request, varCode):
    headerText = 'Sectors'
    sector = Sectors.objects.get(id = varCode)
    form = SectorsForm(instance = sector)

    if request.method == 'POST':
        form = SectorsForm(request.POST, instance = sector)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewsector')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deletesector(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Sector'
    returnUrl = 'viewsector'

    deletedVal = Sectors.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewsector')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.sector,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## Designations
@admin_only
def viewdesignations(request):
    headerText = 'Designations'
    createData = 'createdesignation'
    designations = Designations.objects.all()

    context  = {
        'designations' : designations,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createdesignation(request):
    headerText = 'Designations'
    form = DesignationForm()

    if request.method == 'POST':
        form = DesignationForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewdesignations') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editdesignation(request, varCode):
    headerText = 'Designations'
    designation = Designations.objects.get(id = varCode)
    form = DesignationForm(instance = designation)

    if request.method == 'POST':
        form = DesignationForm(request.POST, instance = designation)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewdesignations')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deletedesignation(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Designations'
    returnUrl = 'viewdesignations'

    deletedVal = Designations.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewdesignations')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.designation,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## Gender
@admin_only
def viewgenders(request):
    headerText = 'Genders'
    createData = 'creategender'
    genders = Gender.objects.all()

    context  = {
        'genders' : genders,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def creategender(request):
    headerText = 'Genders'
    form = GenderForm()

    if request.method == 'POST':
        form = GenderForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewgenders') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editgender(request, varCode):
    headerText = 'Genders'
    gender = Gender.objects.get(id = varCode)
    form = GenderForm(instance = gender)

    if request.method == 'POST':
        form = GenderForm(request.POST, instance = gender)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewgenders')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deletegender(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Gender'
    returnUrl = 'viewgenders'

    deletedVal = Gender.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewgenders')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)



## Employment Status
@admin_only
def viewempstatus(request):
    headerText = 'Employment Status'
    createData = 'createempstatus'
    empstatus = EmploymentStatus.objects.all()

    context  = {
        'empstatus' : empstatus,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createempstatus(request):
    headerText = 'Employment Status'
    form = EmploymentStatusForm()

    if request.method == 'POST':
        form = EmploymentStatusForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewempstatus') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editempstatus(request, varCode):
    headerText = 'Employment Status'
    empstatus = EmploymentStatus.objects.get(id = varCode)
    form = EmploymentStatusForm(instance = empstatus)

    if request.method == 'POST':
        form = EmploymentStatusForm(request.POST, instance = empstatus)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewempstatus')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deleteempstatus(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Employment Status'
    returnUrl = 'viewempstatus'

    deletedVal = EmploymentStatus.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewempstatus')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.status,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## Employment Type
@admin_only
def viewemptypes(request):
    headerText = 'Employment Types'
    createData = 'createemptype'
    emptypes = EmploymentType.objects.all()

    context  = {
        'emptypes' : emptypes,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def createemptype(request):
    headerText = 'Employment Type'
    form = EmploymentTypeForm()

    if request.method == 'POST':
        form = EmploymentTypeForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewemptypes') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def editemptype(request, varCode):
    headerText = 'Employment Type'
    emptype = EmploymentType.objects.get(id = varCode)
    form = EmploymentTypeForm(instance = emptype)

    if request.method == 'POST':
        form = EmploymentTypeForm(request.POST, instance = emptype)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewemptypes')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def deleteemptype(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Employment Type'
    #returnUrl = 'viewemptypes'

    deletedVal = EmploymentType.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewemptypes')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.employmentType,
        #'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)






## Identity Types
@admin_only
def viewidentitytypes(request):
    headerText = 'Identity Types'
    createData = 'createidentitytype'
    identitytypes = IdentityTypes.objects.all()

    context  = {
        'identitytypes' : identitytypes,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createidentitytype(request):
    headerText = 'Identity Types'
    form = IdentityTypeForm()

    if request.method == 'POST':
        form = IdentityTypeForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewidentitytypes') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editidentitytype(request, varCode):
    headerText = 'Identity Types'
    identitytype = IdentityTypes.objects.get(id = varCode)
    form = IdentityTypeForm(instance = identitytype)

    if request.method == 'POST':
        form = IdentityTypeForm(request.POST, instance = identitytype)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewidentitytypes')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deleteidentitytype(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Identity Type'
    returnUrl = 'viewidentitytypes'

    deletedVal = IdentityTypes.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewidentitytypes')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)





## Marital Status
@admin_only
def viewmaritalstatus(request):
    headerText = 'Marital Status'
    createData = 'createmaritalstatus'
    maritalstatus = MaritalStatus.objects.all()

    context  = {
        'maritalstatus' : maritalstatus,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createmaritalstatus(request):
    headerText = 'Marital Status'
    form = MaritalStatusForm()

    if request.method == 'POST':
        form = MaritalStatusForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewmaritalstatus') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def editmaritalstatus(request, varCode):
    headerText = 'Marital Status'
    maritalstatus = MaritalStatus.objects.get(id = varCode)
    form = MaritalStatusForm(instance = maritalstatus)

    if request.method == 'POST':
        form = MaritalStatusForm(request.POST, instance = maritalstatus)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewmaritalstatus')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def deletemaritalstatus(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Marital Status'
    returnUrl = 'viewmaritalstatus'

    deletedVal = MaritalStatus.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewmaritalstatus')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)






## Degree

def viewdegrees(request):
    headerText = 'Degrees'
    createData = 'createdegree'
    degrees = Degree.objects.all()

    context  = {
        'degrees' : degrees,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def createdegree(request):
    headerText = 'Degree'
    form = DegreeForm()

    if request.method == 'POST':
        form = DegreeForm(request.POST)
        try:
            if form.is_valid():
                data = form.save()
                return redirect('viewdegrees') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editdegree(request, varCode):
    headerText = 'Degree'
    degree = Degree.objects.get(id = varCode)
    form = DegreeForm(instance = degree)

    if request.method == 'POST':
        form = DegreeForm(request.POST, instance = degree)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewdegrees')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deletedegree(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Degree'
    returnUrl = 'viewdegrees'

    deletedVal = Degree.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewdegrees')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.degreeName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)





## Institute
@admin_only
def viewinstitutes(request):
    headerText = 'Institutions'
    createData = 'createinstitute'
    institutes = Institution.objects.all()

    context  = {
        'institutes' : institutes,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createinstitute(request):
    headerText = 'Institutions'
    form = InstitutionForm()

    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        try:
            if form.is_valid():
                data = form.save()
                return redirect('viewinstitutes') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editinstitute(request, varCode):
    headerText = 'Institutions'
    institute = Institution.objects.get(id = varCode)
    form = InstitutionForm(instance = institute)

    if request.method == 'POST':
        form = InstitutionForm(request.POST, instance = institute)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewinstitutes')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deleteinstitute(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Institution'
    returnUrl = 'viewinstitutes'

    deletedVal = Institution.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewinstitutes')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## Employee Organizations
@admin_only
def viewemporganizations(request):
    headerText = 'Companies'
    createData = 'createemporg'
    companies = EmpOrganizations.objects.all().order_by('name')

    context  = {
        'companies' : companies,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createemporg(request):
    headerText = 'Companies'
    form = EmployeeOrgForm()

    if request.method == 'POST':
        form = EmployeeOrgForm(request.POST)
        try:
            if form.is_valid():
                data = form.save()
                return redirect('viewemporganizations') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def editemporg(request, varCode):
    headerText = 'Companies'
    company = EmpOrganizations.objects.get(id = varCode)
    form = EmployeeOrgForm(instance = company)

    if request.method == 'POST':
        form = EmployeeOrgForm(request.POST, instance = company)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewemporganizations')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def deleteemporg(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Company'
    returnUrl = 'viewemporganizations'

    deletedVal = EmpOrganizations.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewemporganizations')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




######################################################################################################
## Employees
######################################################################################################

@admin_only
def viewemployees(request):
    headerText = 'Employees'
    createData = 'createemployee'
    employees = Employees.objects.all()

    context  = {
        'employees' : employees,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def viewemployeedetails(request, empId):
    emp = Employees.objects.get(id = empId)
    empaddresses = emp.employeeaddress_set.all()
    presentaddress = emp.employeeaddress_set.filter(addressType = 'Present')
    permanentaddress = emp.employeeaddress_set.filter(addressType = 'Permanent')
    empdegree = emp.employeedegree_set.all()
    empwork = emp.employmenthistory_set.all()
    
    try:
        emergencycontact = EmpEmergencyContact.objects.get(employees = emp)
    except EmpEmergencyContact.DoesNotExist:
        emergencycontact = None


    context  = {
        'emp' : emp,
        'empaddresses' : empaddresses,
        'presentaddress' : presentaddress,
        'permanentaddress' : permanentaddress,
        'empdegree' : empdegree,
        'empwork' : empwork,
        'emergencycontact' : emergencycontact,
    }
    return render(request, 'hrms/profile.html', context)



@admin_only
def createemployee(request):
    headerText = 'Employees'
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewemployees') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)







@admin_only
def editemployee(request, varCode):
    headerText = 'Employees'
    employee = Employees.objects.get(id = varCode)
    form = EmployeeForm(instance = employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance = employee)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewemployees')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deleteemployee(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Employee'
    returnUrl = 'viewemployees'

    deletedVal = Employees.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewemployees')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.get_emp_name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def load_designations(request):
    sector_id = request.GET.get('sector')
    
    designations = Designations.objects.filter(sector_id=sector_id) 
    
    

    context = {
        'designations' : designations,   
    }
    return render(request, 'hrms/designation_ddlist.html', context)




## EMPLOYEE ADDRESS
@admin_only
def createempaddress(request, empId):
    headerText = 'Employee Address'
    emp = Employees.objects.get(id = empId)
    form = EmployeeAddressForm()

    if request.method == 'POST':
        form = EmployeeAddressForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.employees = emp
                data.save()
                return redirect('viewemployees') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)






## EMPLOYEE DEGREE
@admin_only
def createempdegree(request, empId):
    headerText = 'Employee Degree'

    emp = Employees.objects.get(id = empId)

    form = EmployeeDegreeForm()

    if request.method == 'POST':
        form = EmployeeDegreeForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.employees = emp
                data.save()
                return redirect('viewemployeedetails', empId = empId) 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## EMPLOYEE WORK HISTORY
@admin_only
def createempwork(request, empId):
    headerText = 'Employment History'

    emp = Employees.objects.get(id = empId)

    form = EmployeeWorkForm()

    if request.method == 'POST':
        form = EmployeeWorkForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.employees = emp
                data.save()
                return redirect('viewemployeedetails', empId = empId) 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## EMPLOYEE EMERGENCY CONTACT
@admin_only
def createemergencycontact(request, empId):
    headerText = 'Employment Emergency Contact'

    emp = Employees.objects.get(id = empId)

    form = EmergencyContactForm()

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.employees = emp
                data.save()
                return redirect('viewemployeedetails', empId = empId) 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def editemergencycontact(request, empId, varCode):
    headerText = 'Employee Emergency Contact'
    emp = Employees.objects.get(id = empId)
    employee = EmpEmergencyContact.objects.get(id = varCode)
    
    form = EmergencyContactForm(instance = employee)

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, request.FILES, instance = employee)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewemployeedetails', empId = empId)
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



#################################################################################################
####    ATTENDANCE
#################################################################################################
@login_required(login_url='login')
def viewattendance(request):
    headerText = 'Attendance'
    createData = 'createattendance'

    
    emp = Employees.objects.get(user = request.user)
    attendance = emp.attendance_set.all().order_by('-attendanceDate')
    attendanceToday = emp.attendance_set.filter(attendanceDate = datetime.date.today())

    context  = {
        'attendance' : attendance,
        'emp' : emp,
        'attendanceToday' : attendanceToday,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def viewattendanceall(request):
    headerText = 'Attendance for Today'
    createData = 'createattendance'

    attendance = Attendance.objects.filter(attendanceDate = datetime.date.today())    
    

    context  = {
        'attendance' : attendance,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def viewattendanceold(request):
    headerText = 'Attendance for Today'
    createData = 'createattendance'

    
    attendance = Attendance.objects.all().exclude(employees__grades__grade = 'CXO').order_by('-attendanceDate')
    

    context  = {
        'attendance' : attendance,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def editattendance(request, varCode):
    headerText = 'Edit Attendance Data'

    attendance = Attendance.objects.get(id = varCode)

    form = EditAttendanceForm(instance = attendance)

    if request.method == 'POST':
        form = EditAttendanceForm(request.POST, instance = attendance)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewattendanceall')
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@login_required(login_url='login')
def checkin(request):
    headerText = 'Attendance'
    emp = Employees.objects.get(user = request.user)
    #adate = timezone.localtime()
    attendance = Attendance.objects.create(employees = emp, attendanceDate = datetime.date.today(), checkIn = datetime.datetime.now())
    #attendance = Attendance.objects.create(employees = emp, attendanceDate = adate.date, checkIn = adate)
    attendance.save()

    return redirect('viewattendance')



@login_required(login_url='login')
def checkout(request, varId):
    headerText = 'Attendance'
    
    attendance = Attendance.objects.get(id= varId)
    attendance.checkOut = datetime.datetime.now()
    #attendance.checkOut = timezone.localtime()
    attendance.save()

    return redirect('viewattendance')





#############################################################################################################

## PROFILE

@login_required(login_url='login')
def empprofile(request):

    emp = Employees.objects.get(user = request.user)
    empaddresses = emp.employeeaddress_set.all()
    presentaddress = emp.employeeaddress_set.filter(addressType = 'Present')
    permanentaddress = emp.employeeaddress_set.filter(addressType = 'Permanent')
    empdegree = emp.employeedegree_set.all()
    empwork = emp.employmenthistory_set.all()
    
    try:
        emergencycontact = EmpEmergencyContact.objects.get(employees = emp)
    except EmpEmergencyContact.DoesNotExist:
        emergencycontact = None


    context  = {
        'emp' : emp,
        'empaddresses' : empaddresses,
        'presentaddress' : presentaddress,
        'permanentaddress' : permanentaddress,
        'empdegree' : empdegree,
        'empwork' : empwork,
        'emergencycontact' : emergencycontact,
    }
    return render(request, 'hrms/profile.html', context)



@login_required(login_url='login')
def createaddress(request, empId, addressType):
    headerText = 'Add Present Address'
    emp = Employees.objects.get(id = empId)
    form = EditEmployeeAddressForm()

    if request.method == 'POST':
        form = EditEmployeeAddressForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.employees = emp
                data.addressType = addressType
                data.save()
                return redirect('viewemployeedetails', empId = empId) 
        except Exception as e:
            messages.error(request, str(e))

    context ={
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@login_required(login_url='login')
def editaddress(request, varId):
    headerText = 'Add Present Address'
    empaddress = EmployeeAddress.objects.get(id = varId)
    form = EditEmployeeAddressForm(instance = empaddress)

    if request.method == 'POST':
        form = EditEmployeeAddressForm(request.POST, instance = empaddress)
        try:
            if form.is_valid():
                data = form.save()
                return redirect('viewemployeedetails', empId = empaddress.employees.id) 
        except Exception as e:
            messages.error(request, str(e))

    context ={
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)






## Shifting Types

def viewshifttypes(request):
    headerText = 'Shift Types'
    createData = 'createshift'
    shifttypes = ShiftType.objects.all()

    context  = {
        'shifttypes' : shifttypes,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



def createshift(request):
    headerText = 'Shift Types'
    form = ShiftForm()

    if request.method == 'POST':
        form = ShiftForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewshifttypes') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def editshift(request, varCode):
    headerText = 'Shift Types'
    shift = ShiftType.objects.get(id = varCode)
    form = ShiftForm(instance = shift)

    if request.method == 'POST':
        form = ShiftForm(request.POST, instance = shift)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewshifttypes')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def deleteshift(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Shift Type'
    returnUrl = 'viewshifttypes'

    deletedVal = ShiftType.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewshifttypes')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.shiftName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## Religions

def viewreligions(request):
    headerText = 'Religions'
    createData = 'createreligion'
    religions = Religions.objects.all()

    context  = {
        'religions' : religions,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



def createreligion(request):
    headerText = 'Religions'
    form = ReligionForm()

    if request.method == 'POST':
        form = ReligionForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewreligions') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def editreligion(request, varCode):
    headerText = 'Religion'
    religion = Religions.objects.get(id = varCode)
    form = ReligionForm(instance = religion)

    if request.method == 'POST':
        form = ReligionForm(request.POST, instance = religion)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewreligions')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def deletereligion(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Religion'
    returnUrl = 'viewreligios'

    deletedVal = Religions.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewreligions')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.shiftName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)







################################################################################################
##############              TEAM INFO          #################################################
################################################################################################



## My Team
@login_required(login_url='login')
def viewmyteams(request):
    headerText = 'Team Information'
    createButton = 'No'
    manager = Employees.objects.get(user = request.user)
    myteam = manager.employees_set.all().order_by('first_name')
    context = {
        'headerText' : headerText,
        'createButton' : createButton,
        'myteam' : myteam,
    }
    return render(request, 'blockzenmaster/view.html', context)



# employee wise attendance
@login_required(login_url='login')
def viewempattendance(request, EmpId):
    headerText = 'Employee Attendance'
    createButton = 'No'
    employee = Employees.objects.get(id = EmpId)    
    empattendance = employee.attendance_set.all().order_by('-id')
    context = {
        'headerText' : headerText,
        'createButton' : createButton,
        'employee' : employee,
        'empattendance' : empattendance,
    }
    return render(request, 'blockzenmaster/view.html', context)