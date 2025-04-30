from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('main/', views.main, name='main'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/json/', views.get_teachers, name='get_teachers'),
    path('teachers/create/', views.create_teacher, name='create_teacher'), 
    path('students/', views.student_list, name='student_list'), 
    path('students/json/', views.get_students, name='get_students'),
    path('students/create/', views.create_student, name='create_student'), 
    path('classes/', views.class_list, name='class_list'),  
    path('classes/json/', views.get_classes, name='get_classes'), 
    path('admin/', admin.site.urls),
]
