from django.urls import path
from accesscontrol import views
from django.contrib.auth import views as auth_views

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

    path('resetuserpassword/<str:varCode>', views.resetuserpassword, name = 'resetuserpassword'),


    # RESET PASSWORD (djangor by default reset password views ase..see doc)
    # 1st step: submit email form..akta mail newar jonno form banabo jekhane reset link jabe
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accesscontrol/password_reset.html"), name='reset_password'),
    # 2nd step: mail e link ta pathanor por akta success message dekhabe
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accesscontrol/password_reset_sent.html"), name='password_reset_done'),
    # 3rd step: link to password reset form
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accesscontrol/password_reset_form.html"), name='password_reset_confirm'),
    # 4th step: password successfully changed
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accesscontrol/password_reset_done.html"), name='password_reset_complete'),
    # erpor settings.py e SMTP config korte hobe


    

]