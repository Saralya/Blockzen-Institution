from django.urls import path
from hrms import views

urlpatterns = [

    ## CHANGE PASSWORD
    path('changepassword', views.changepassword, name = 'changepassword'),

    ## DIVISIONS
    path('viewdivisions', views.viewdivisions, name = 'viewdivisions'),
    path('createdivision', views.createdivision, name = 'createdivision'),
    path('editdivision/<str:varCode>', views.editdivision, name = 'editdivision'),
    path('deletedivision/<str:varCode>', views.deletedivision, name = 'deletedivision'),


    ## DEPARTMENTS
    path('viewdepartments', views.viewdepartments, name = 'viewdepartments'),
    path('createdepartment', views.createdepartment, name = 'createdepartment'),
    path('editdepartment/<str:varCode>', views.editdepartment, name = 'editdepartment'),
    path('deletedepartment/<str:varCode>', views.deletedepartment, name = 'deletedepartment'),


    ## GRADES
    path('viewgrades', views.viewgrades, name = 'viewgrades'),
    path('creategrade', views.creategrade, name = 'creategrade'),
    path('editgrade/<str:varCode>', views.editgrade, name = 'editgrade'),
    path('deletegrade/<str:varCode>', views.deletegrade, name = 'deletegrade'),


    ## DESIGNATION
    path('viewdesignations', views.viewdesignations, name = 'viewdesignations'),
    path('createdesignation', views.createdesignation, name = 'createdesignation'),
    path('editdesignation/<str:varCode>', views.editdesignation, name = 'editdesignation'),
    path('deletedesignation/<str:varCode>', views.deletedesignation, name = 'deletedesignation'),


    ## GENDER
    path('viewgenders', views.viewgenders, name = 'viewgenders'),
    path('creategender', views.creategender, name = 'creategender'),
    path('editgender/<str:varCode>', views.editgender, name = 'editgender'),
    path('deletegender/<str:varCode>', views.deletegender, name = 'deletegender'),


    ## EMPLOYMENT STATUS
    path('viewempstatus', views.viewempstatus, name = 'viewempstatus'),
    path('createempstatus', views.createempstatus, name = 'createempstatus'),
    path('editempstatus/<str:varCode>', views.editempstatus, name = 'editempstatus'),
    path('deleteempstatus/<str:varCode>', views.deleteempstatus, name = 'deleteempstatus'),
    


    ## EMPLOYMENT TYPES
    path('viewemptypes', views.viewemptypes, name = 'viewemptypes'),
    path('createemptype', views.createemptype, name = 'createemptype'),
    path('editemptype/<str:varCode>', views.editemptype, name = 'editemptype'),
    path('deleteemptype/<str:varCode>', views.deleteemptype, name = 'deleteemptype'),
    


    ## IDENTITY TYPES
    path('viewidentitytypes', views.viewidentitytypes, name = 'viewidentitytypes'),
    path('createidentitytype', views.createidentitytype, name = 'createidentitytype'),
    path('editidentitytype/<str:varCode>', views.editidentitytype, name = 'editidentitytype'),
    path('deleteidentitytype/<str:varCode>', views.deleteidentitytype, name = 'deleteidentitytype'),


    ## MARITAL STATUS
    path('viewmaritalstatus', views.viewmaritalstatus, name = 'viewmaritalstatus'),
    path('createmaritalstatus', views.createmaritalstatus, name = 'createmaritalstatus'),
    path('editmaritalstatus/<str:varCode>', views.editmaritalstatus, name = 'editmaritalstatus'),
    path('deletemaritalstatus/<str:varCode>', views.deletemaritalstatus, name = 'deletemaritalstatus'),


    ## DEGREE
    path('viewdegrees', views.viewdegrees, name = 'viewdegrees'),
    path('createdegree', views.createdegree, name = 'createdegree'),
    path('editdegree/<str:varCode>', views.editdegree, name = 'editdegree'),
    path('deletedegree/<str:varCode>', views.deletedegree, name = 'deletedegree'),

    ## Institution
    path('viewinstitutes', views.viewinstitutes, name = 'viewinstitutes'),
    path('createinstitute', views.createinstitute, name = 'createinstitute'),
    path('editinstitute/<str:varCode>', views.editinstitute, name = 'editinstitute'),
    path('deleteinstitute/<str:varCode>', views.deleteinstitute, name = 'deleteinstitute'),


    ## Employee Organizations
    path('viewemporganizations', views.viewemporganizations, name = 'viewemporganizations'),
    path('createemporg', views.createemporg, name = 'createemporg'),
    path('editemporg/<str:varCode>', views.editemporg, name = 'editemporg'),
    path('deleteemporg/<str:varCode>', views.deleteemporg, name = 'deleteemporg'),
    

    ## SHIFT TYPES
    path('viewshifttypes', views.viewshifttypes, name = 'viewshifttypes'),
    path('createshift', views.createshift, name = 'createshift'),
    path('editshift/<str:varCode>', views.editshift, name = 'editshift'),
    path('deleteshift/<str:varCode>', views.deleteshift, name = 'deleteshift'),


    ## RELIGIONS
    path('viewreligions', views.viewreligions, name = 'viewreligions'),
    path('createreligion', views.createreligion, name = 'createreligion'),
    path('editreligion/<str:varCode>', views.editreligion, name = 'editreligion'),
    path('deletereligion/<str:varCode>', views.deletereligion, name = 'deletereligion'),

    


    ## EMPLOYEES
    path('viewemployees', views.viewemployees, name = 'viewemployees'),
    path('createemployee', views.createemployee, name = 'createemployee'),
    path('editemployee/<str:varCode>', views.editemployee, name = 'editemployee'),
    path('deleteemployee/<str:varCode>', views.deleteemployee, name = 'deleteemployee'),
    # Employee Details
    path('viewemployeedetails/<str:empId>', views.viewemployeedetails, name = 'viewemployeedetails'),
    # Address
    path('createempaddress/<str:empId>', views.createempaddress, name = 'createempaddress'),
    path('createaddress/<str:empId>/<str:addressType>', views.createaddress, name = 'createaddress'),
    path('editaddress/<str:varId>', views.editaddress, name = 'editaddress'),
    # Degree
    path('createempdegree/<str:empId>', views.createempdegree, name = 'createempdegree'),
    # Work History
    path('createempwork/<str:empId>', views.createempwork, name = 'createempwork'),
    # Emergency Contact
    path('createemergencycontact/<str:empId>', views.createemergencycontact, name = 'createemergencycontact'),
    path('editemergencycontact/<str:empId>/<str:varCode>', views.editemergencycontact, name = 'editemergencycontact'),


    ## Employee Profile
    path('empprofile', views.empprofile, name = 'empprofile'),


    ## ATTENDANCE
    path('viewattendance', views.viewattendance, name = 'viewattendance'),
    path('createattendance', views.createemployee, name = 'createattendance'),
    path('checkin', views.checkin, name = 'checkin'),
    path('checkout/<str:varId>', views.checkout, name = 'checkout'),


    path('viewattendanceall', views.viewattendanceall, name = 'viewattendanceall'),
    path('editattendance/<str:varCode>', views.editattendance, name = 'editattendance'),

    path('viewattendanceold', views.viewattendanceold, name = 'viewattendanceold'),


    ######## MANAGER URLS
    ## MY TEAM
    path('viewmyteams', views.viewmyteams, name = 'viewmyteams'),
    path('viewempattendance/<str:EmpId>', views.viewempattendance, name = 'viewempattendance'),


]