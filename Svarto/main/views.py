from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
from .models import Teacher, Student, Class

def main(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def get_teachers(request):
    teachers = Teacher.objects.all()
    teacher_list = [{"name": f"{teacher.first_name} {teacher.last_name}"} for teacher in teachers]
    return JsonResponse(teacher_list, safe=False)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def get_students(request):
    students = Student.objects.all()
    student_list = [{"name": f"{student.first_name} {student.last_name}", "class": student.class_id.class_name} for student in students]
    return JsonResponse(student_list, safe=False)

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})

def get_classes(request):
    classes = Class.objects.all()
    class_list = [{"class_name": class_obj.class_name, 
                   "students": [f"{student.first_name} {student.last_name}" for student in class_obj.students.all()]} 
                  for class_obj in classes]
    return JsonResponse(class_list, safe=False)
