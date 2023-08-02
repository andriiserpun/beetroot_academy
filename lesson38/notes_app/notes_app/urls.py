from django.urls import path
from notes.views import hello_view

urlpatterns = [
    path('hello/', hello_view, name='hello-view'),
]
