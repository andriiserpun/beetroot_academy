from django.contrib import admin
from django.urls import path
from book_store.views import *

urlpatterns = [
    path("load_data/", async_load_data)
]
