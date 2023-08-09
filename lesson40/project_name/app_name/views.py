
from django.shortcuts import render

from lesson40.project_name.app_name.models import Note


def home(request):

    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})
