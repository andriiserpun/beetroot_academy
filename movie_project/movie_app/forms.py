from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['user_first_name', 'title', 'year', 'country', 'comment']

    title = forms.CharField(label='Title', max_length=100)
    user_first_name = forms.CharField(label='Your First Name', max_length=50)

class RandomFilmForm(forms.Form):
    watched = forms.BooleanField(label='I watched', required=False)
    show_another = forms.BooleanField(label='Another random film', required=False)