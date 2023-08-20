from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.shortcuts import render
from django.http import HttpResponse
import random
from random import choice
from .forms import RandomFilmForm
from django.contrib.auth.decorators import login_required

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
    year_filter = request.GET.get('year')
    country_filter = request.GET.get('country')
    user_first_name_filter = request.GET.get('user_first_name')

    movies = Movie.objects.all()

    if year_filter and year_filter != 'None':
        try:
            year_filter = int(year_filter)
            movies = movies.filter(year=year_filter)
        except ValueError:
            pass

    if country_filter and country_filter != 'None':
        movies = movies.filter(country=country_filter)

    if user_first_name_filter and user_first_name_filter != 'None':
        movies = movies.filter(user_first_name=user_first_name_filter)

    context = {
        'movies': movies,
        'year_filter': year_filter,
        'country_filter': country_filter,
        'user_first_name_filter': user_first_name_filter,
    }
    return render(request, 'movie_app/movie_list.html', context)


# Create your views here.
