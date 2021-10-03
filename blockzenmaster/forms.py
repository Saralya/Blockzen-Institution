from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blockzenmaster.models import *


from django.contrib.admin import widgets


import datetime

## Date Picker

class DateInput(forms.DateInput):
    input_type = 'date'







## User Administration


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditUserForm(ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active']


###################################################################################################
###################################################################################################
###################################################################################################



class CountryForm(ModelForm):
    countryName = forms.CharField(max_length=100, label = 'Country Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    currencyCode = forms.CharField(max_length=200, label = 'Currency Code', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Countries
        fields = ['countryName', 'currencyCode']


class RegionForm(ModelForm):
    regionName = forms.CharField(max_length=100, label = 'Region/Division Name', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Regions
        fields = ['regionName', 'countries']

    def __init__(self, *args, **kwargs):
        super(RegionForm, self).__init__(*args, **kwargs)

        self.fields['countries'].widget.attrs['class'] = 'form-control'
        self.fields['countries'].label = 'Country Name'



class CityForm(ModelForm):
    cityName = forms.CharField(max_length=100, label = 'City Name', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Cities
        fields = ['cityName', 'regions']

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)

        self.fields['regions'].widget.attrs['class'] = 'form-control'
        self.fields['regions'].label = 'Region/Division Name'



class OrganizationForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Organization Name', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Organization
        fields = ['name']



class BranchForm(ModelForm):
    name = forms.CharField(max_length=200, label = 'Branch Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=500, label = 'Address', widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))
    area = forms.CharField(max_length=200, label = 'Area', widget=forms.TextInput(attrs={'class':'form-control'}))
    postCode = forms.CharField(max_length=200, label = 'Post Code', widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = Branch
        fields = ['organization', 'name', 'address', 'area', 'cities', 'postCode']

    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)

        self.fields['organization'].widget.attrs['class'] = 'form-control'
        self.fields['organization'].label = 'Organization'
        self.fields['cities'].widget.attrs['class'] = 'form-control'
        self.fields['cities'].label = 'City'





