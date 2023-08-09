from django.test import TestCase
from university.models import *
from university.forms import *
class FormTestCase(TestCase):
    def setUp(self):
        Discipline.objects.create(id=7, discipline_name='PH', teacher=None)
        Room.objects.create(id=7, academy_building='Main Building', room_number=101)
        Student.objects.create(id=7, first_name='John', last_name='Doe', birth_date='2000-05-15')
    def test_teacher_form_positive(self):
        data = {
            'first_name': 'Ivan',
            'last_name': 'Borodii',
            'salary': 50000,
        }
        form = TeacherModelForm(data=data)
        self.assertTrue(form.is_valid())

    def test_teacher_form_negative(self):
        data = {
            'first_name': 'Ivan',
            'last_name': 'Borodii',
            'salary': 'abc',
        }
        form = TeacherModelForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_schedule_positive(self):
        student = Student.objects.first()
        discipline = Discipline.objects.first()
        room = Room.objects.first()
        data = {
            'student': student.pk,
            'discipline': discipline.pk,
            'start_time': '2023-05-01 09:00:00',
            'end_time': '2023-05-01 11:00:00',
            'room': room.pk,
            'lesson_type': 'lecture',
        }
        form = ScheduleForm(data=data)
        self.assertTrue(form.is_valid())