from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ims.forms import *
from blockzenmaster.models import *
from blockzenmaster.decorators import admin_only
from .filters import StudentRegistrationFilter

# Create your views here.

def viewstudentstatus(request):
    headerText = 'Student Status'
    createData = 'createstudentstatus'
    studentstatus = StudentStatus.objects.all()

    context  = {
        'studentstatus' : studentstatus,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createstudentstatus(request):
    headerText = 'Divisions'
    form = StudentStatusForm()

    if request.method == 'POST':
        form = StudentStatusForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewstudentstatus') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editstudentstatus(request, varCode):
    headerText = 'Branches'
    studentstatus = StudentStatus.objects.get(id = varCode)
    form = StudentStatusForm(instance = studentstatus)

    if request.method == 'POST':
        form = StudentStatusForm(request.POST, instance = studentstatus)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewstudentstatus')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletestudentstatus(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Student Status'
    returnUrl = 'viewstudentstatus'

    deletedVal = StudentStatus.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewstudentstatus')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewstudents(request):
    headerText = 'Students'
    createData = 'createstudents'
    students = Students.objects.all()

    context  = {
        'students' : students,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createstudents(request):
    headerText = 'Students'
    form = StudentsForm()

    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewstudents') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editstudents(request, varCode):
    headerText = 'Students'
    students = Students.objects.get(id = varCode)
    form = StudentsForm(instance = students)

    if request.method == 'POST':
        form = StudentsForm(request.POST, request.FILES, instance = students)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewstudents')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletestudents(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Student'
    returnUrl = 'viewstudents'

    deletedVal = Students.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewstudents')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewparents(request):
    headerText = 'Parents'
    createData = 'createparents'
    parents = Parents.objects.all()

    context  = {
        'parents' : parents,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createparents(request):
    headerText = 'Parents'
    form = ParentsForm()

    if request.method == 'POST':
        form = ParentsForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewparents') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editparents(request, varCode):
    headerText = 'Parents'
    parents = Parents.objects.get(id = varCode)
    form = ParentsForm(instance = parents)

    if request.method == 'POST':
        form = ParentsForm(request.POST, instance = parents)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewparents')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deleteparents(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Parent'
    returnUrl = 'viewparents'

    deletedVal = Parents.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewparents')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewlocalgurdian(request):
    headerText = 'Local Gurdian'
    createData = 'createlocalgurdian'
    localgurdian = LocalGuardian.objects.all()

    context  = {
        'localgurdian' : localgurdian,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createlocalgurdian(request):
    headerText = 'Local Gurdian'
    form = LocalGuardianForm()

    if request.method == 'POST':
        form = LocalGuardianForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewlocalgurdian') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editlocalgurdian(request, varCode):
    headerText = 'Local Gurdian'
    localgurdian = LocalGuardian.objects.get(id = varCode)
    form = LocalGuardianForm(instance = localgurdian)

    if request.method == 'POST':
        form = LocalGuardianForm(request.POST, instance = localgurdian)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewlocalgurdian')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletelocalgurdian(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Local Gurdian'
    returnUrl = 'viewlocalgurdian'

    deletedVal = LocalGuardian.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewlocalgurdian')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewclasses(request):
    headerText = 'Classes'
    createData = 'createclasses'
    classes = Classes.objects.all()

    context  = {
        'classes' : classes,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createclasses(request):
    headerText = 'Classes'
    form = ClassesForm()

    if request.method == 'POST':
        form = ClassesForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewclasses') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editclasses(request, varCode):
    headerText = 'Classes'
    classes = Classes.objects.get(id = varCode)
    form = ClassesForm(instance = classes)

    if request.method == 'POST':
        form = ClassesForm(request.POST, instance = classes)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewclasses')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deleteclasses(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Class'
    returnUrl = 'viewclasses'

    deletedVal = Classes.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewclasses')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)

def viewsection(request):
    headerText = 'Section'
    createData = 'createsection'
    section = Section.objects.all()

    context  = {
        'section' : section,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createsection(request):
    headerText = 'Section'
    form = SectionForm()

    if request.method == 'POST':
        form = SectionForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewsection') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editsection(request, varCode):
    headerText = 'Section'
    section = Section.objects.get(id = varCode)
    form = SectionForm(instance = section)

    if request.method == 'POST':
        form = SectionForm(request.POST, instance = section)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewsection')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletesection(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Section'
    returnUrl = 'viewsection'

    deletedVal = Section.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewsection')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewsubject(request):
    headerText = 'Subject'
    createData = 'createsubject'
    subject = Subject.objects.all()

    context  = {
        'subject' : subject,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createsubject(request):
    headerText = 'Subject'
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewsubject') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editsubject(request, varCode):
    headerText = 'Section'
    subject = Subject.objects.get(id = varCode)
    form = SubjectForm(instance = subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance = subject)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewsubject')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletesubject(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Subject'
    returnUrl = 'viewsubject'

    deletedVal = Subject.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewsubject')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewsessions(request):
    headerText = 'Sessions'
    createData = 'createsessions'
    sessions = Sessions.objects.all()

    context  = {
        'sessions' : sessions,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createsessions(request):
    headerText = 'Sessions'
    form = SessionsForm()

    if request.method == 'POST':
        form = SessionsForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewsessions') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editsessions(request, varCode):
    headerText = 'Sessions'
    sessions = Sessions.objects.get(id = varCode)
    form = SessionsForm(instance = sessions)

    if request.method == 'POST':
        form = SessionsForm(request.POST, instance = sessions)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewsessions')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletesessions(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Sessions'
    returnUrl = 'viewsessions'

    deletedVal = Sessions.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewsessions')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewmediumtype(request):
    headerText = 'Medium Type'
    createData = 'createmediumtype'
    mediumtype = MediumType.objects.all()

    context  = {
        'mediumtype' : mediumtype,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createmediumtype(request):
    headerText = 'Medium Type'
    form = MediumTypeForm()

    if request.method == 'POST':
        form = MediumTypeForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewmediumtype') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editmediumtype(request, varCode):
    headerText = 'Medium Type'
    mediumtype = MediumType.objects.get(id = varCode)
    form = MediumTypeForm(instance = mediumtype)

    if request.method == 'POST':
        form = MediumTypeForm(request.POST, instance = mediumtype)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewmediumtype')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletemediumtype(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Session'
    returnUrl = 'viewmediumtype'

    deletedVal = MediumType.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewmediumtype')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewclassdetail(request):
    headerText = 'Class Detail'
    createData = 'createclassdetail'
    classdetail = ClassDetail.objects.all()

    context  = {
        'classdetail' : classdetail,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createclassdetail(request):
    headerText = 'Class Detail'
    form = ClassDetailForm()

    if request.method == 'POST':
        form = ClassDetailForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewclassdetail') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editclassdetail(request, varCode):
    headerText = 'Class Detail'
    classdetail = ClassDetail.objects.get(id = varCode)
    form = ClassDetailForm(instance = classdetail)

    if request.method == 'POST':
        form = ClassDetailForm(request.POST, instance = classdetail)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewclassdetail')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deleteclassdetail(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Class Detail'
    returnUrl = 'viewclassdetail'

    deletedVal = ClassDetail.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewclassdetail')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewclasssubject(request):
    headerText = 'Class Subject'
    createData = 'createclasssubject'
    classsubject = ClassSubject.objects.all()

    context  = {
        'classsubject' : classsubject,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createclasssubject(request):
    headerText = 'Class Subject'
    form = ClassSubjectForm()

    if request.method == 'POST':
        form = ClassSubjectForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewclasssubject') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editclasssubject(request, varCode):
    headerText = 'Class Subject'
    classsubject = ClassSubject.objects.get(id = varCode)
    form = ClassSubjectForm(instance = classsubject)

    if request.method == 'POST':
        form = ClassSubjectForm(request.POST, instance = classsubject)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewclasssubject')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deleteclasssubject(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Class Subject'
    returnUrl = 'viewclasssubject'

    deletedVal = ClassSubject.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewclasssubject')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewteachersubject(request):
    headerText = 'Teacher Subject'
    createData = 'createteachersubject'
    teachersubject = TeacherSubject.objects.all()

    context  = {
        'teachersubject' : teachersubject,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createteachersubject(request):
    headerText = 'Teacher Subject'
    form = TeacherSubjectForm()

    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewteachersubject') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editteachersubject(request, varCode):
    headerText = 'Teacher Subject'
    teachersubject = TeacherSubject.objects.get(id = varCode)
    form = TeacherSubjectForm(instance = teachersubject)

    if request.method == 'POST':
        form = TeacherSubjectForm(request.POST, instance = teachersubject)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewteachersubject')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deleteteachersubject(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Teacher Subject'
    returnUrl = 'viewteachersubject'

    deletedVal = TeacherSubject.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewteachersubject')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def viewstudentregistration(request):
    headerText = 'Student Registration'
    createData = 'createstudentregistration'
    studentregistration = StudentRegistration.objects.all()

    context  = {
        'studentregistration' : studentregistration,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)


def createstudentregistration(request):
    headerText = 'Student Registration'
    form = StudentRegistrationForm()

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewstudentregistration') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editstudentregistration(request, varCode):
    headerText = 'Student Registration'
    studentregistration = StudentRegistration.objects.get(id = varCode)
    form = StudentRegistrationForm(instance = studentregistration)

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance = studentregistration)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewstudentregistration')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletestudentregistration(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Student Registration'
    returnUrl = 'viewstudentregistration'

    deletedVal = StudentRegistration.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewstudentregistration')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)





def searchstudents(request):
    headerText = 'Search Students'
   
    student = StudentRegistration.objects.all()
    
    myFilter = StudentRegistrationFilter(request.GET, queryset=student)

    student = myFilter.qs
    

    context  = {
        
        'headerText' : headerText,
        'myFilter' : myFilter,
        'student' : student
        
    }
    return render(request, 'blockzenmaster/entry.html', context)


def studentattendance(request):
    headerText = 'Student Attendance'
   
    student = StudentRegistration.objects.all()
    
    myFilter = StudentRegistrationFilter(request.GET, queryset=student)

    student = myFilter.qs
    

    context  = {
        
        'headerText' : headerText,
        'myFilter' : myFilter,
        'student' : student
        
    }
    return render(request, 'blockzenmaster/entry.html', context)

def saveattendance(request):
    studentId = request.GET.get('userId')
    attendance = request.GET.get('attval')

    obj = StudentAttendance.objects.create(student= Students.objects.get(id=studentId) ,isPresent=attendance)
    obj.save()


def viewstudentattendance(request):
    headerText = 'View attendance'
    createData = 'studentattendance'
    attendance = StudentAttendance.objects.all()
    
    context = {
        'headerText' : headerText,
        'attendance' : attendance,
        'createData' : createData,
    }
    return render(request, 'ims/imsview.html', context)
    
    

    


def viewdetails(request, varCode):
    headerText = 'Student Profile'
    student = Students.objects.get(id = varCode)

    

    context = {
        'student' : student,
        
        'headerText' : headerText,

    }
    return render(request, 'ims/studentprofile.html',context )


def load_branches(request):
    org_id = request.GET.get('organization')
    branch = Branch.objects.filter(organization_id=org_id).order_by('name') 
    

    context = {
        'branch' : branch,   
    }
    return render(request, 'ims/branch_ddlist.html',context)


def load_classes(request):
    branch_id = request.GET.get('branch')
    classes = Classes.objects.filter(branch_id=branch_id).order_by('className') 
    

    context = {
        'classes' : classes,   
    }
    return render(request, 'ims/class_ddlist.html',context)


def load_sections(request):
    class_id = request.GET.get('classes')
    sections = Section.objects.filter(classes_id=class_id).order_by('sectionName') 
    

    context = {
        'sections' : sections,   
    }
    return render(request, 'ims/section_ddlist.html',context)


def load_teachers(request):
    subject_id = request.GET.get('subject')
    teachers = TeacherSubject.objects.filter(subject_id=subject_id)
    

    context = {
        'teachers' : teachers,   
    }
    return render(request, 'ims/teacher_ddlist.html',context)


