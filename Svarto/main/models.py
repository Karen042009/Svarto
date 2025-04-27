from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    class_name = models.CharField(max_length=20)
    teachers = models.ManyToManyField(Teacher, related_name='classes')

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

class Gradebook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='gradebooks')

class Grade(models.Model):
    gradebook = models.ForeignKey(Gradebook, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    grade = models.IntegerField()