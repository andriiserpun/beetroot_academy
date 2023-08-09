from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Note
from .views import index

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('index')

    def test_index_view_with_post_request(self):
        data = {
            'title': 'Test Note',
            'text': 'This is a test note.',
            'reminder': '2023-08-10',
            'category': 'General'
        }
        request = self.factory.post(self.url, data)
        response = index(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)
        note = Note.objects.first()
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.text, 'This is a test note.')
        self.assertEqual(note.reminder, '2023-08-10')
        self.assertEqual(note.category, 'General')

    def test_index_view_with_get_request(self):
        request = self.factory.get(self.url)
        response = index(request)

        self.assertEqual(response.status_code, 200)


    # Add more test cases as needed



# Create your tests here.
