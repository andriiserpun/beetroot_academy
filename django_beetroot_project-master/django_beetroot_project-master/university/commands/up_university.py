from university.models import *
from django.db import connection

def disable_foreign_keys():
    with connection.cursor() as cursor:
        cursor.execute("SET session_replication_role = 'replica';")

def enable_foreign_keys():
    with connection.cursor() as cursor:
        cursor.execute("SET session_replication_role = 'origin';")

disable_foreign_keys()

Teacher.objects.all().delete()
StudyGroup.objects.all().delete()
Student.objects.all().delete()
Room.objects.all().delete()
Discipline.objects.all().delete()
Schedule.objects.all().delete()

enable_foreign_keys()

study_groups = [
StudyGroup(study_group='SC-1', faculty='Faculty of Science')         ,
StudyGroup(study_group='SC-2', faculty='Faculty of Science')         ,
StudyGroup(study_group='EG-1', faculty='Faculty of Engineering')     ,
StudyGroup(study_group='EG-2', faculty='Faculty of Engineering')     ,
StudyGroup(study_group='BS-1', faculty='Faculty of Business')
]
students = [
Student(id=1, first_name='John', last_name='Doe', birth_date='2000-05-15', study_group_id='SC-1')              ,
Student(id=2, first_name='Jane', last_name='Smith', birth_date='1999-10-03', study_group_id='SC-1')            ,
Student(id=3, first_name='Robert', last_name='Johnson', birth_date='2001-02-28', study_group_id='SC-2')        ,
Student(id=4, first_name='Emily', last_name='Brown', birth_date='2002-07-20', study_group_id='SC-2')           ,
Student(id=5, first_name='Michael', last_name='Wilson', birth_date='2000-12-12', study_group_id='EG-1')        ,
Student(id=6, first_name='Sophia', last_name='Martinez', birth_date='2001-09-05', study_group_id='EG-1')       ,
Student(id=7, first_name='David', last_name='Taylor', birth_date='2001-03-10', study_group_id='EG-2')          ,
Student(id=8, first_name='Olivia', last_name='Anderson', birth_date='2000-06-25', study_group_id='EG-2')       ,
Student(id=9, first_name='Daniel', last_name='Thomas', birth_date='2002-04-18', study_group_id='BS-1')         ,
Student(id=10, first_name='Ava', last_name='Clark', birth_date='2000-11-30', study_group_id='BS-1')
]

teachers = [
Teacher(id=1, first_name='Michael', last_name='Johnson', salary=1000)               ,
Teacher(id=2, first_name='Sarah', last_name='Smith', salary=1400)                   ,
Teacher(id=3, first_name='Christopher', last_name='Davis', salary=2300)             ,
Teacher(id=4, first_name='Emily', last_name='Anderson', salary=1700)                ,
Teacher(id=5, first_name='Daniel', last_name='Wilson', salary=7600)                 ,
Teacher(id=6, first_name='Sophia', last_name='Taylor', salary=1450)                 ,
Teacher(id=7, first_name='Oliver', last_name='Martin', salary=4120)                 ,
Teacher(id=8, first_name='Isabella', last_name='Thomas', salary=2200)               ,
Teacher(id=9, first_name='James', last_name='Brown', salary=3400)                   ,
Teacher(id=10, first_name='Emma', last_name='Clark', salary=5500)
]

disciplines = [
Discipline(id=1, discipline_name='MA', teacher_id=1)    ,
Discipline(id=2, discipline_name='LI', teacher_id=2)    ,
Discipline(id=3, discipline_name='PH', teacher_id=3)    ,
Discipline(id=4, discipline_name='CH', teacher_id=3)    ,
Discipline(id=5, discipline_name='CO', teacher_id=4)    ,
Discipline(id=6, discipline_name='HI', teacher_id=5)    ,
Discipline(id=7, discipline_name='GE', teacher_id=5)    ,
Discipline(id=8, discipline_name='BI', teacher_id=6)    ,
Discipline(id=9, discipline_name='EC', teacher_id=7)    ,
Discipline(id=10, discipline_name='AR', teacher_id=7)
]

rooms = [
Room(id=1, academy_building='Building A', room_number=101) ,
Room(id=2, academy_building='Building A', room_number=202) ,
Room(id=3, academy_building='Building B', room_number=303) ,
Room(id=4, academy_building='Building B', room_number=403) ,
Room(id=5, academy_building='Building C', room_number=104)
]

schedule = [
Schedule(id=1, student_id=1, discipline_id=1, start_time='2023-01-01 09:00:00', end_time='2023-01-01 11:00:00', room_id=1, lesson_type='Lecture')   ,
Schedule(id=2, student_id=2, discipline_id=2, start_time='2023-01-01 14:00:00', end_time='2023-01-01 16:00:00', room_id=2, lesson_type='Lab')
]


StudyGroup.objects.bulk_create(study_groups)
Student.objects.bulk_create(students)
Teacher.objects.bulk_create(teachers)
Discipline.objects.bulk_create(disciplines)
Room.objects.bulk_create(rooms)
Schedule.objects.bulk_create(schedule)
