from django.test import TestCase, Client
from university.models import *
from django.urls import reverse

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.teacher_data = {'first_name': 'John',
                             'last_name': 'Doe',
                             'salary': 5000}

    def test_view_data(self):
        teacher_1 = Teacher.objects.create(id=1, first_name='John', last_name='Doe', salary=5000)
        teacher_2 = Teacher.objects.create(id=2, first_name='Jane', last_name='Smith', salary=6000)
        Discipline.objects.create(id=1, discipline_name='MA', teacher=teacher_1)
        Discipline.objects.create(id=2, discipline_name='PH', teacher=teacher_2)

        response = self.client.get(reverse("view_data"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['teachers']), 2)
        self.assertEqual(len(response.context['disciplines']), 2)
        self.assertEqual(response.context['max_salary'], 6000)
        self.assertEqual(response.context['min_salary'], 5000)
        self.assertEqual(response.context['avg_salary'], 5500)
        self.assertEqual(response.context['count_teachers'], 2)

    def test_teacher_form_view(self):
        response = self.client.post(reverse("teacher_form_view"), data=self.teacher_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/university/success/')
        self.assertTrue(Teacher.objects.filter(**self.teacher_data).exists())

