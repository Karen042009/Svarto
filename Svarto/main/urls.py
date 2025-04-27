from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('main/', views.main, name='main'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/json/', views.get_teachers, name='get_teachers'),
    path('admin/', admin.site.urls),
]
