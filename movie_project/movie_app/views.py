from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'movie_app/home.html')

def add_comment(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_app/add_comment.html', {'form': form})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/movie_list.html', {'movies': movies})


# Create your views here.
