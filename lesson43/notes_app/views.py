from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_detail', note_id=form.instance.id)
    else:
        form = NoteForm()

    return render(request, 'create_note.html', {'form': form})


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()

    form = NoteForm(instance=note)
    return render(request, 'note_detail.html', {'note': note, 'form': form})


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})
