from django.db import models


class StudyGroup(models.Model):
    study_group = models.CharField(primary_key=True, max_length=5)
    faculty = models.CharField(max_length=100)


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, related_name="studygroup_student", null=True)


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField(null=True)


class Discipline(models.Model):
    disciplines_acro = [
        ('MA', 'Mathematics'),
        ('LI', 'Literature'),
        ('PH', 'Physics'),
        ('CH', 'Chemistry'),
        ('CO', 'Computer Science'),
        ('HI', 'History'),
        ('GE', 'Geography'),
        ('BI', 'Biology'),
        ('EC', 'Economics'),
        ('AR', 'Art')
    ]
    id = models.IntegerField(primary_key=True)
    discipline_name = models.CharField(max_length=2, choices=disciplines_acro)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher_discipline", null=True)


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    academy_building = models.CharField(max_length=100)
    room_number = models.IntegerField()


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, related_name="student_schedule", null=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name="discipline_schedule", null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_schedule", null=True)
    lesson_type = models.CharField(max_length=100)