"""
URL configuration for lesson43 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from notes_app import views
from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('notes/', views.note_list, name='note_list'),
    path('', views.home_view, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]