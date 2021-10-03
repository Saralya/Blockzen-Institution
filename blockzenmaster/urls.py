from django.urls import path
from blockzenmaster import views

urlpatterns = [
    path('', views.home, name = 'home'),


    ###################################################################################
    ### LOCATIONS

    path('viewcountries', views.viewcountries, name = 'viewcountries'),
    path('createcountry', views.createcountry, name = 'createcountry'),
    path('editcountry/<str:varCode>', views.editcountry, name = 'editcountry'),
    path('deletecountry/<str:varCode>', views.deletecountry, name = 'deletecountry'),

    path('viewregions', views.viewregions, name = 'viewregions'),
    path('createregion', views.createregion, name = 'createregion'),
    path('editregion/<str:varCode>', views.editregion, name = 'editregion'),
    path('deleteregion/<str:varCode>', views.deleteregion, name = 'deleteregion'),

    path('viewcities', views.viewcities, name = 'viewcities'),
    path('createcity', views.createcity, name = 'createcity'),
    path('editcity/<str:varCode>', views.editcity, name = 'editcity'),
    path('deletecity/<str:varCode>', views.deletecity, name = 'deletecity'),


    path('vieworganizations', views.vieworganizations, name = 'vieworganizations'),
    path('createorganization', views.createorganization, name = 'createorganization'),
    path('editorganization/<str:varCode>', views.editorganization, name = 'editorganization'),
    path('deleteorganization/<str:varCode>', views.deleteorganization, name = 'deleteorganization'),


    path('viewbranches', views.viewbranches, name = 'viewbranches'),
    path('createbranch', views.createbranch, name = 'createbranch'),
    path('editbranch/<str:varCode>', views.editbranch, name = 'editbranch'),
    path('deletebranch/<str:varCode>', views.deletebranch, name = 'deletebranch'),
]