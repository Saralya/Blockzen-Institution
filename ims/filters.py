import django_filters

from django import forms

from blockzenmaster.models import *


class StudentRegistrationFilter(django_filters.FilterSet):

    
    
    class Meta:
        model = StudentRegistration
        
        fields = ['organization', 'branch', 'classes', 'section', 'roll', 'subject']

    
    

    

    

    