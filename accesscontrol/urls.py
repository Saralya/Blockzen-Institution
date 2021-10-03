from django.urls import path
from accesscontrol import views

urlpatterns = [
    path('login', views.userlogin, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),

    path('viewuser', views.viewuser, name = 'viewuser'),
    path('createuser', views.createuser, name = 'createuser'),
    path('edituser/<str:varCode>', views.edituser, name = 'edituser'),


    ## User Group
    path('viewusergroups', views.viewusergroups, name = 'viewusergroups'),
    path('createusergroup', views.creategroup, name = 'createusergroup'),
    path('assignusergroups/<str:varID>', views.assignusergroups, name = 'assignusergroups'),


    ## CHANGE PASSWORD
    path('changepassword', views.changepassword, name = 'changepassword'),
]