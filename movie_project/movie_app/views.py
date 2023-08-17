from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.shortcuts import render
from django.http import HttpResponse
import random
from random import choice
from .forms import RandomFilmForm

def home(request):
    return render(request, 'movie_app/home.html')

def random_film(request):
    if request.method == 'POST':
        if 'watched' in request.POST:
            random_film = Movie.objects.filter(viewed=False).order_by('?').first()
            if random_film:
                random_film.viewed = True
                random_film.save()
        return redirect('random_film')

    random_film = Movie.objects.filter(viewed=False).order_by('?').first()
    context = {'random_film': random_film}
    return render(request, 'movie_app/random_film.html', context)

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
    if request.method == 'POST':
        for key in request.POST:
            if key.startswith('watched'):
                movie_id = key.split('-')[-1]
                movie = Movie.objects.get(pk=movie_id)
                movie.viewed = True
                movie.save()
        return redirect('movie_list')

    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie_app/movie_list.html', context)



# Create your views here.
