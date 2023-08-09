from django.test import TestCase
from university.models import *
from datetime import date, datetime, timezone

class ModelTestCase(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(id=1,
                               first_name="Pavlo",
                               last_name="Zibrov",
                               salary=5000)

        self.discipline = Discipline.objects.create(id=1,
                               discipline_name="PH",
                               teacher=self.teacher)

        self.room = Room.objects.create(id=1,
                                        academy_building='Main Building',
                                        room_number=101)
        self.study_group = StudyGroup.objects.create(study_group='SG01',
                                                     faculty='Computer Science')
        self.student = Student.objects.create(id=1,
                                              first_name='Alice',
                                              last_name='Smith',
                                              birth_date='1995-05-10',
                                              study_group=self.study_group)

        self.schedule = Schedule.objects.create(id=1,
                                                student=self.student,
                                                discipline=self.discipline,
                                                start_time='2023-07-31 10:00:00',
                                                end_time='2023-07-31 12:00:00',
                                                room=self.room,
                                                lesson_type='Lecture')
    def test_adding_teacher(self):
        self.assertTrue(isinstance(self.teacher, Teacher))
        db_teacher = Teacher.objects.get(id=1)
        self.assertEqual(self.teacher, db_teacher)
        db_teacher_is_exists = Teacher.objects.filter(id=1).exists()
        self.assertTrue(db_teacher_is_exists)

    def test_adding_room(self):
        room = Room.objects.get(id=1)
        self.assertEqual(room, self.room)

    def test_adding_studygroup(self):
        study_group = StudyGroup.objects.get(study_group='SG01')
        self.assertEqual(study_group.faculty, self.study_group.faculty)

    def test_adding_discipline(self):
        discipline = Discipline.objects.get(id=1)
        self.assertEqual(discipline.get_discipline_name_display(), "Physics")
        self.assertEqual(discipline.teacher, self.teacher)

    def test_adding_student(self):
        student = Student.objects.get(id=1)
        self.assertEqual(student.first_name + " " + student.last_name,
                         "Alice Smith")
        self.assertEqual(student.birth_date, date(1995, 5, 10))
        self.assertEqual(student.study_group, self.study_group)

    def test_adding_schedule(self):
        schedule = Schedule.objects.get(id=1)
        self.assertEqual(schedule.student, self.student)
        self.assertEqual(schedule.discipline, self.discipline)
        self.assertEqual(schedule.room, self.room)
        self.assertEqual(schedule.start_time, datetime(2023,7,31,10,0,0,tzinfo=timezone.utc))
        self.assertEqual(schedule.end_time, datetime(2023, 7, 31, 12, 0, 0, tzinfo=timezone.utc))

    def test_update_study_group(self):
        study_group = StudyGroup.objects.get(study_group='SG01')
        study_group.faculty = "Computer Engineering"
        study_group.save()

        updated_study_group = StudyGroup.objects.get(study_group='SG01')
        self.assertEqual(updated_study_group.faculty, "Computer Engineering")

    def test_delete_teacher(self):
        teacher = Teacher.objects.get(id=1)
        teacher.delete()

        self.assertFalse(Teacher.objects.filter(id=1).exists())
        self.assertFalse(Discipline.objects.filter(id=1).exists())
        self.assertFalse(Schedule.objects.filter(id=1).exists())

    def test_delete_student(self):
        student = Student.objects.get(id=1)
        student.delete()

        self.assertFalse(Student.objects.filter(id=1).exists())
        schedule = Schedule.objects.get(id=1)
        self.assertIsNone(schedule.student)