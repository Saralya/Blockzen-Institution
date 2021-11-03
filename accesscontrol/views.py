from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from accesscontrol.forms import *
from blockzenmaster.decorators import admin_only
from ims import views
from hrms import views


## LOGIN
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)    
            return redirect('home')
            #group = None
            #if request.user.groups.exists():
            #    group = request.user.groups.all()[0].name
            #if group == 'admin':
            #    return redirect('home')  
            #else:
            #    return redirect('employeehome')

        else:
            messages.info(request,'User name or password is incorrect.')
            

    context = {}
    return render(request, 'accesscontrol/login.html',context)


## LOGOUT
def logout_user(request):
    logout(request)
    return redirect('login')



########################################################################################################
## USER ADMINISTRATION
########################################################################################################

## USER GROUP
@admin_only
def viewusergroups(request):
    headerText = 'User Groups'
    createData = 'createusergroup'


    groups = Group.objects.all()

    context = {
        'headerText' : headerText,
        'groups' : groups,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def creategroup(request):
    headerText = 'Uesr Group'
    

    if request.method == 'POST':        
        try:
            userGroup = request.POST.get('strGroupName')
            data = Group.objects.create(name = userGroup)
            data.save()
            return redirect('viewusergroups') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {        
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def assignusergroups(request, varID):
    headerText = 'Add User to Groups'

    groups = Group.objects.get(id= varID)

    users = User.objects.all()

    if request.method == 'POST':
        userName = request.POST.get('username')
        userId = User.objects.get(username = userName)
        groups.user_set.add(userId)
        return redirect('viewuser')

    context = {
        'headerText' : headerText,
        'groups' : groups,
        'users' : users,
    }
    return render(request, 'blockzenmaster/entry.html', context)





@admin_only
def viewuser(request):
    headerText = 'Users'
    createData = 'createuser'

    users = User.objects.all()

    context = {
        'headerText' : headerText,
        'createData' : createData,
        'users' : users,
    }
    return render(request, 'blockzenmaster/view.html', context)


@admin_only
def createuser(request):
    headerText = 'Users'

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()            
            uname = form.cleaned_data.get('username')
        
            group = form.cleaned_data.get('groups')
            data = list(group.values())  # eta korlam karon group will return a queryset..etake list na banale data access kora jabe na
            print(data[0]["name"])
            

            if data[0]["name"] == 'Student':         
                
                
                return redirect('createstudents')

            else:
                 return redirect('createemployee')


        
    context = {
        'headerText' : headerText,
        'form': form,
        }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def edituser(request, varCode):
    headerText = 'Users'

    user = User.objects.get(id = varCode)

    form = EditUserForm(instance = user)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance = user)

        if form.is_valid():
            user = form.save()            
            uname = form.cleaned_data.get('username')           

            return redirect('viewuser')        
        
    context = {
        'headerText' : headerText,
        'form': form,
        }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def resetuserpassword(request, varCode):
    headerText = 'Users'

    user = User.objects.get(id = varCode)

    form = ResetUserPasswordForm(instance = user)

    if request.method == "POST":
        form = ResetUserPasswordForm(request.POST, instance = user)

        if form.is_valid():
            user = form.save()            
            # uname = form.cleaned_data.get('username')           

            return redirect('viewuser')        
        
    context = {
        'headerText' : headerText,
        'form': form,
        }
    return render(request, 'blockzenmaster/entry.html', context)




@login_required(login_url='login')
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