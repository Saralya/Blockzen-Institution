from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blockzenmaster.forms import *
from blockzenmaster.models import *
from blockzenmaster.decorators import admin_only



def home(request):
    return render(request, 'blockzenmaster/home.html',{})



###############################################################################################
### LOCATION
###############################################################################################

## Country
@admin_only
def viewcountries(request):
    headerText = 'Countries'
    createData = 'createcountry'
    countries = Countries.objects.all()

    context  = {
        'countries' : countries,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@login_required(login_url='login')
def createcountry(request):
    headerText = 'Countries'
    form = CountryForm()

    if request.method == 'POST':
        form = CountryForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewcountries') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def editcountry(request, varCode):
    headerText = 'Countries'
    country = Countries.objects.get(id = varCode)
    form = CountryForm(instance = country)

    if request.method == 'POST':
        form = CountryForm(request.POST, instance = country)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewcountries')  
        except Exception as e:
            messages.error(request, str(e))  


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def deletecountry(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Country'
    returnUrl = 'viewcountries'

    deletedVal = Countries.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewcountries')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.countryName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)



## Division

def viewregions(request):
    headerText = 'Regions'
    createData = 'createregion'
    divisions = Regions.objects.all()

    context  = {
        'divisions' : divisions,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


def createregion(request):
    headerText = 'Regions'
    form = RegionForm()

    if request.method == 'POST':
        form = RegionForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewregions') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def editregion(request, varCode):
    headerText = 'Regions'
    division = Regions.objects.get(id = varCode)
    form = RegionForm(instance = division)

    if request.method == 'POST':
        form = RegionForm(request.POST, instance = division)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewregions')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)




def deleteregion(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Regions'
    returnUrl = 'viewregions'

    deletedVal = Regions.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewregions')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.regionName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)



## Cities

def viewcities(request):
    headerText = 'Cities'
    createData = 'createcity'
    cities = Cities.objects.all()

    context  = {
        'cities' : cities,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)


def createcity(request):
    headerText = 'Cities'
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewcities') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



def editcity(request, varCode):
    headerText = 'Cities'
    cities = Cities.objects.get(id = varCode)
    form = CityForm(instance = cities)

    if request.method == 'POST':
        form = CityForm(request.POST, instance = cities)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewcities')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


def deletecity(request, varCode):
    headerText = 'Delete'
    deletedItem = 'City'
    returnUrl = 'viewcities'

    deletedVal = Cities.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewcities')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.cityName,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## Organization
@admin_only
def vieworganizations(request):
    headerText = 'Organizations'
    createData = 'createorganization'
    orgs = Organization.objects.all()

    context  = {
        'orgs' : orgs,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createorganization(request):
    headerText = 'Organizations'
    form = OrganizationForm()

    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('vieworganizations') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def editorganization(request, varCode):
    headerText = 'Organization'
    org = Organization.objects.get(id = varCode)
    form = OrganizationForm(instance = org)

    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance = org)
        try:
            if form.is_valid():
                form.save()
                return redirect('vieworganizations')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)



@admin_only
def deleteorganization(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Organization'
    returnUrl = 'vieworganizations'

    deletedVal = Organization.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('vieworganizations')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)




## Branch
@admin_only
def viewbranches(request):
    headerText = 'Branches'
    createData = 'createbranch'
    branches = Branch.objects.all()

    context  = {
        'branches' : branches,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'blockzenmaster/view.html', context)



@admin_only
def createbranch(request):
    headerText = 'Branches'
    form = BranchForm()

    if request.method == 'POST':
        form = BranchForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdby = request.user
                data.save()
                return redirect('viewbranches') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def editbranch(request, varCode):
    headerText = 'Branches'
    branch = Branch.objects.get(id = varCode)
    form = BranchForm(instance = branch)

    if request.method == 'POST':
        form = BranchForm(request.POST, instance = branch)
        try:
            if form.is_valid():
                form.save()
                return redirect('viewbranches')   
        except Exception as e:
            messages.error(request, str(e)) 


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'blockzenmaster/entry.html', context)


@admin_only
def deletebranch(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Branch'
    returnUrl = 'viewbranches'

    deletedVal = Branch.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewbranches')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
        'returnUrl' : returnUrl,
    }
    return render(request, 'blockzenmaster/entry.html', context)
