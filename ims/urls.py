from django.urls import path
from ims import views

urlpatterns = [
    
    path('viewstudentstatus', views.viewstudentstatus, name = 'viewstudentstatus'),
    path('createstudentstatus', views.createstudentstatus, name = 'createstudentstatus'),
    path('editstudentstatus/<str:varCode>', views.editstudentstatus, name = 'editstudentstatus'),
    path('deletestudentstatus/<str:varCode>', views.deletestudentstatus, name = 'deletestudentstatus'),


    path('viewstudents', views.viewstudents, name = 'viewstudents'),
    path('createstudents', views.createstudents, name = 'createstudents'),
    path('editstudents/<str:varCode>', views.editstudents, name = 'editstudents'),
    path('deletestudents/<str:varCode>', views.deletestudents, name = 'deletestudents'),

    path('viewparents', views.viewparents, name = 'viewparents'),
    path('createparents', views.createparents, name = 'createparents'),
    path('editparents/<str:varCode>', views.editparents, name = 'editparents'),
    path('deleteparents/<str:varCode>', views.deleteparents, name = 'deleteparents'),

    path('viewlocalgurdian', views.viewlocalgurdian, name = 'viewlocalgurdian'),
    path('createlocalgurdian', views.createlocalgurdian, name = 'createlocalgurdian'),
    path('editlocalgurdian/<str:varCode>', views.editlocalgurdian, name = 'editlocalgurdian'),
    path('deletelocalgurdian/<str:varCode>', views.deletelocalgurdian, name = 'deletelocalgurdian'),

    path('viewclasses', views.viewclasses, name = 'viewclasses'),
    path('createclasses', views.createclasses, name = 'createclasses'),
    path('editclasses/<str:varCode>', views.editclasses, name = 'editclasses'),
    path('deleteclasses/<str:varCode>', views.deleteclasses, name = 'deleteclasses'),

    path('viewsection', views.viewsection, name = 'viewsection'),
    path('createsection', views.createsection, name = 'createsection'),
    path('editsection/<str:varCode>', views.editsection, name = 'editsection'),
    path('deletesection/<str:varCode>', views.deletesection, name = 'deletesection'),

    path('viewsubject', views.viewsubject, name = 'viewsubject'),
    path('createsubject', views.createsubject, name = 'createsubject'),
    path('editsubject/<str:varCode>', views.editsubject, name = 'editsubject'),
    path('deletesubject/<str:varCode>', views.deletesubject, name = 'deletesubject'),

    path('viewsessions', views.viewsessions, name = 'viewsessions'),
    path('createsessions', views.createsessions, name = 'createsessions'),
    path('editsessions/<str:varCode>', views.editsessions, name = 'editsessions'),
    path('deletesessions/<str:varCode>', views.deletesessions, name = 'deletesessions'),

    path('viewmediumtype', views.viewmediumtype, name = 'viewmediumtype'),
    path('createmediumtype', views.createmediumtype, name = 'createmediumtype'),
    path('editmediumtype/<str:varCode>', views.editmediumtype, name = 'editmediumtype'),
    path('deletemediumtype/<str:varCode>', views.deletemediumtype, name = 'deletemediumtype'),

    path('viewclassdetail', views.viewclassdetail, name = 'viewclassdetail'),
    path('createclassdetail', views.createclassdetail, name = 'createclassdetail'),
    path('editclassdetail/<str:varCode>', views.editclassdetail, name = 'editclassdetail'),
    path('deleteclassdetail/<str:varCode>', views.deleteclassdetail, name = 'deleteclassdetail'),

    path('viewclasssubject', views.viewclasssubject, name = 'viewclasssubject'),
    path('createclasssubject', views.createclasssubject, name = 'createclasssubject'),
    path('editclasssubject/<str:varCode>', views.editclasssubject, name = 'editclasssubject'),
    path('deleteclasssubject/<str:varCode>', views.deleteclasssubject, name = 'deleteclasssubject'),

    path('viewteachersubject', views.viewteachersubject, name = 'viewteachersubject'),
    path('createteachersubject', views.createteachersubject, name = 'createteachersubject'),
    path('editteachersubject/<str:varCode>', views.editteachersubject, name = 'editteachersubject'),
    path('deleteteachersubject/<str:varCode>', views.deleteteachersubject, name = 'deleteteachersubject'),

    path('viewstudentregistration', views.viewstudentregistration, name = 'viewstudentregistration'),
    path('createstudentregistration', views.createstudentregistration, name = 'createstudentregistration'),
    path('editstudentregistration/<str:varCode>', views.editstudentregistration, name = 'editstudentregistration'),
    path('deletestudentregistration/<str:varCode>', views.deletestudentregistration, name = 'deletestudentregistration'),


    path('searchstudents', views.searchstudents, name = 'searchstudents'),
    path('studentattendance', views.studentattendance, name = 'studentattendance'),
    path('saveattendance', views.saveattendance, name = 'saveattendance'),
    path('viewstudentattendance', views.viewstudentattendance, name = 'viewstudentattendance'),

    path('viewdetails/<str:varCode>', views.viewdetails, name = 'viewdetails'),

    path('ajax/load_branches/', views.load_branches, name='ajax_load_branches'),
    path('ajax/load_classes/', views.load_classes, name='ajax_load_classes'),
    path('ajax/load_sections/', views.load_sections, name='ajax_load_sections'),

    path('ajax/load_teachers/', views.load_teachers, name='ajax_load_teachers'),
]