from django.contrib import admin
from django.urls import path
from university.views import *

urlpatterns = [
    path("view_data/", view_data, name="view_data"),
    path("success/", SuccessView.as_view(), name="success_view"),
    path("add_teacher/", teacher_form_view, name="teacher_form_view"),
    path("add_schedule/", schedule_form_view, name="schedule_form_view"),
    path("add_student/", student_form_view, name="student_form_view"),
    path("add_room/", room_form_view, name="room_form_view"),
    path("add_study_group/", study_group_form_view, name="study_group_form_view"),
    path("teachers/", get_teachers_data),
    path("teachers/<int:pk>", get_single_teacher),
    path("schedules/", get_schedules_data),
    path("schedules/<int:pk>", get_single_schedule),
    path("login/", sign_in),
    path("logout/", sign_out),
    path("signup/", sign_up)
]
