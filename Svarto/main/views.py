from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
from .models import Teacher

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

def create_teachers(request):
    Teacher.objects.create(first_name="Կարեն", last_name="Պետրոսյան")
    Teacher.objects.create(first_name="Անի", last_name="Հովհաննիսյան")
    return HttpResponse("Teachers have been added.")
