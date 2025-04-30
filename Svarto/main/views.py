from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
from .models import Teacher, Student, Class
from django.views.decorators.csrf import csrf_exempt
import json


def main(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


# Աշակերտների ցուցակի json տեսք
def get_students(request):
    students = Student.objects.all()
    student_list = [
        {
            "id": student.id,
            "name": f"{student.first_name} {student.last_name}",
            "class": student.class_id.class_name,
        }
        for student in students
    ]
    return JsonResponse(student_list, safe=False)


# Աշակերտ ստեղծելու ֆունկցիա
@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        class_id = data.get("class_id")

        try:
            class_instance = Class.objects.get(id=class_id)
            student = Student.objects.create(
                first_name=first_name, last_name=last_name, class_id=class_instance
            )
            return JsonResponse(
                {
                    "status": "ok",
                    "student_id": student.id,
                }
            )
        except Class.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Դասարանը չի գտնվել"}, status=400
            )

    return JsonResponse(
        {"status": "error", "message": "Մեթոդը թույլատրելի չէ"}, status=405
    )


def class_list(request):
    classes = Class.objects.all()
    return render(request, "class_list.html", {"classes": classes})


def get_classes(request):
    classes = Class.objects.all()
    class_list = [
        {
            "id": class_obj.id,
            "class_name": class_obj.class_name,
            "teachers": [
                {"id": teacher.id, "name": f"{teacher.first_name} {teacher.last_name}"}
                for teacher in class_obj.teachers.all()
            ],
            "students": [
                {"id": student.id, "name": f"{student.first_name} {student.last_name}"}
                for student in class_obj.students.all()
            ],
        }
        for class_obj in classes
    ]
    return JsonResponse(class_list, safe=False)


@csrf_exempt
def create_teacher(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        if first_name and last_name:
            teacher = Teacher.objects.create(first_name=first_name, last_name=last_name)
            return JsonResponse(
                {
                    "status": "ok",
                    "teacher_id": teacher.id,
                }
            )
        else:
            return JsonResponse(
                {"status": "error", "message": "Բոլոր դաշտերը պարտադիր են"}, status=400
            )

    return JsonResponse(
        {"status": "error", "message": "Մեթոդը թույլատրելի չէ"}, status=405
    )


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def get_teachers(request):
    teachers = Teacher.objects.all()
    teacher_list = [
        {"id": teacher.id, "name": f"{teacher.first_name} {teacher.last_name}"}
        for teacher in teachers
    ]
    return JsonResponse(teacher_list, safe=False)
