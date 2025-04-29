from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
from .models import Teacher, Student, Class
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.csrf import csrf_exempt

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
    class_list = [{
        "class_name": class_obj.class_name, 
        "teachers": [f"{teacher.first_name} {teacher.last_name}" for teacher in class_obj.teachers.all()],
        "students": [f"{student.first_name} {student.last_name}" for student in class_obj.students.all()]
    } for class_obj in classes]
    
    return JsonResponse(class_list, safe=False)

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        class_id = data.get('class_id')

        try:
            class_instance = Class.objects.get(id=class_id)
            Student.objects.create(first_name=first_name, last_name=last_name, class_id=class_instance)
            return JsonResponse({'status': 'ok'})
        except Class.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Դասարանը չի գտնվել'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Մեթոդը թույլատրելի չէ'}, status=405)
