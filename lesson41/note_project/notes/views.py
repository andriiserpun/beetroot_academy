from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        reminder = request.POST['reminder']
        category = request.POST['category']
        Note.objects.create(title=title, text=text, reminder=reminder, category=category)
        return redirect('index')

    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})
