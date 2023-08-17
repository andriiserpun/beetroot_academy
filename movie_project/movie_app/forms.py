from django import forms
from .models import Movie
import json

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['user_first_name', 'title', 'year', 'country', 'comment']

    title = forms.CharField(label='Title', max_length=100)
    user_first_name = forms.CharField(label='Your First Name', max_length=50)

class RandomFilmForm(forms.Form):
    watched = forms.BooleanField(label='I watched', required=False)
    show_another = forms.BooleanField(label='Another random film', required=False)

def export_movies_to_json(file_path):
    movies = Movie.objects.all()

    movies_data = []
    for movie in movies:
        movie_data = {
            'user_first_name': movie.user_first_name,
            'title': movie.title,
            'year': movie.year,
            'country': movie.country,
            # Добавьте другие поля модели фильма, если есть
        }
        movies_data.append(movie_data)

    # Запишите данные в JSON файл с указанием ensure_ascii=False
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(movies_data, json_file, indent=4, ensure_ascii=False)

export_movies_to_json('movies_data.json')