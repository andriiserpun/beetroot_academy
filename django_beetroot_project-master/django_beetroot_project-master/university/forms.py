from django import forms
from university.models import Teacher, Schedule, StudyGroup, Discipline, Room, Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class TeacherForm(forms.Form):
    id = forms.IntegerField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    salary = forms.IntegerField()

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ("id",)

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ("id",)

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)

        students_choices = [(student.pk, f"{student.first_name} {student.last_name}") for student in Student.objects.all()]
        self.fields['student'].choices = students_choices

        disciplines_choices = [(discipline.pk, discipline.get_discipline_name_display()) for discipline in Discipline.objects.all()]
        self.fields['discipline'].choices = disciplines_choices


        rooms_choices = [(room.pk, room.room_number) for room in Room.objects.all()]
        self.fields['room'].choices = rooms_choices

class StudyGroupModelForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = "__all__"

class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('id',)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'birth_date', 'study_group')
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        study_group_choices = [(study_group.pk, study_group.study_group) for study_group in StudyGroup.objects.all()]
        self.fields['study_group'].choices = study_group_choices

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']