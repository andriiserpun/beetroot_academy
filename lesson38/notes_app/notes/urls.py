from django.urls import path
from notes.views import hello_view

urlpatterns = [
    path("notes/", include('notes.url'), hello_view, name="hello"),
]
