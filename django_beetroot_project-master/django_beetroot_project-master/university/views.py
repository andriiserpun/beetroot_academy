from django.shortcuts import render, redirect
from university.models import *
from university.forms import *
from django.db.models import Max, Min, Avg
from django.views.generic import TemplateView
from django.urls import get_resolver, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def get_application_urls():
    urls = {}
    for view_name in get_resolver().reverse_dict.keys():
        if isinstance(view_name, str) and view_name.endswith("_form_view"):
            reversed_val = reverse(view_name)
            key = reversed_val.split("/")[2]
            urls[key] = reversed_val
    return urls

def view_data(request):
    teachers = Teacher.objects.all()
    disciplines = Discipline.objects.all()
    max_salary_result = Teacher.objects.aggregate(max_salary=Max('salary'))
    min_salary_result = Teacher.objects.aggregate(min_salary=Min('salary'))
    avg_salary_result = Teacher.objects.aggregate(avg_salary=Avg('salary'))
    count_teachers = Teacher.objects.count()
    context = {"teachers": teachers,
               "disciplines": disciplines,
               "max_salary": max_salary_result['max_salary'],
               "min_salary": min_salary_result['min_salary'],
               "avg_salary": avg_salary_result['avg_salary'],
               "count_teachers": count_teachers}
    return render(request, 'companies.html', context)

@login_required(login_url="home")
def teacher_form_view(request):
    page_name = 'Teacher'
    urls = get_application_urls()
    if request.method == "POST":
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            max_id = Teacher.objects.aggregate(max_id=Max('id'))
            if max_id['max_id'] is None:
                max_id = 1
            else:
                max_id = max_id['max_id'] + 1
            teacher_data = form.cleaned_data
            teacher_data['id'] = max_id
            Teacher.objects.create(**teacher_data)
            return redirect('/university/success/')
        else:
            form = TeacherModelForm
            context = {"form": form,
                       "page_name": page_name,
                       "urls": urls}
            return render(request, "login.html", context)
    else:
        form = TeacherModelForm
        context = {"form": form,
                    "page_name": page_name,
                    "urls": urls}
        return render(request, "login.html", context)

class SuccessView(TemplateView):
    template_name = 'success.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        value = self.request.GET.get('type')
        if value == '1':
            color = 'red'
        elif value == '2':
            color = 'blue'
        elif value == '3':
            color = 'green'
        else:
            color = 'black'
        context["color"] = color
        return context

@login_required(login_url="home")
def schedule_form_view(request):
    page_name = "Schedule"
    urls = get_application_urls()
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            max_id = Schedule.objects.aggregate(max_id=Max('id'))
            if max_id['max_id'] is None:
                id = 1
            else:
                id = max_id['max_id'] + 1
            schedule_data = form.cleaned_data
            schedule_data['id'] = id
            Schedule.objects.create(**schedule_data)
            return redirect("/university/success")
    else:
        form = ScheduleForm()

    context = {
        'form': form,
        "page_name": page_name,
        "urls": urls
    }
    return render(request, 'login.html', context)

@login_required(login_url="home")
def study_group_form_view(request):
    page_name = "Study_Group"
    urls = get_application_urls()
    if request.method == "POST":
        form = StudyGroupModelForm(request.POST)
        if form.is_valid():
            study_group_data = form.cleaned_data
            StudyGroup.objects.create(**study_group_data)
            return redirect('/university/success/')
        else:
            form = StudyGroupModelForm
            context = {"form": form}
            return render(request, "login.html", context)
    else:
        form = StudyGroupModelForm
        context = {"form": form,
                    "page_name": page_name,
                   "urls": urls}
        return render(request, "login.html", context)

@login_required(login_url="home")
def room_form_view(request):
    page_name = "Room"
    urls = get_application_urls()
    if request.method == "POST":
        form = RoomModelForm(request.POST)
        if form.is_valid():
            max_id = Room.objects.aggregate(max_id=Max('id'))
            if max_id['max_id'] is None:
                id = 1
            else:
                id = max_id['max_id'] + 1
            room_data = form.cleaned_data
            room_data['id'] = id
            Room.objects.create(**room_data)
            return redirect('/university/success/')
        else:
            form = RoomModelForm
            context = {"form": form,
                       "page_name": page_name,
                       "urls": urls}
            return render(request, "login.html", context)
    else:
        form = RoomModelForm
        context = {"form": form,
                    "page_name": page_name,
                       "urls": urls}
        return render(request, "login.html", context)

@login_required(login_url="home")
def student_form_view(request):
    page_name = "Student"
    urls = get_application_urls()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            max_id = Student.objects.aggregate(max_id=Max('id'))
            if max_id['max_id'] is None:
                id = 1
            else:
                id = max_id['max_id'] + 1
            student_data = form.cleaned_data
            student_data['id'] = id
            Student.objects.create(**student_data)
            return redirect('/university/success/')
        else:
            form = StudentForm
            context = {"form": form,
                       "page_name": page_name,
                       "urls": urls}
            return render(request, "login.html", context)
    else:
        form = StudentForm
        context = {"form": form,
                    "page_name": page_name,
                   "urls": urls}
        return render(request, "login.html", context)

@login_required
def get_teachers_data(request):
    teachers = Teacher.objects.all()
    context = {"teachers": teachers,
               "page_name": "Teacher"}
    return render(request, "teachers.html", context)

@login_required
def get_single_teacher(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
        disciplines = Discipline.objects.filter(teacher_id=pk)
    except Teacher.DoesNotExist:
        return redirect("/university/teachers")
    context = {"teacher": teacher,
               "page_name": "Teacher",
               "disciplines": disciplines}
    return render(request, "teacher.html", context)

@login_required
def get_schedules_data(request):
    schedules = Schedule.objects.all()
    context = {"schedules": schedules,
               "page_name": "Schedule"}
    return render(request, "schedules.html", context)

@login_required
def get_single_schedule(request, pk):
    try:
        schedule = Schedule.objects.get(id=pk)
    except Schedule.DoesNotExist:
        return redirect("/university/schedules")
    context = {"schedule": schedule,
               "page_name": "Schedule"}
    return render(request, "schedule.html", context)

def view_homepage(request):
    urls = get_application_urls()
    context = {"urls": urls}
    return render(request, 'index.html', context)

def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, 'registration/login.html', context)

def sign_out(request):
    logout(request)
    return redirect('home')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, 'registration/sign_up.html', context)

