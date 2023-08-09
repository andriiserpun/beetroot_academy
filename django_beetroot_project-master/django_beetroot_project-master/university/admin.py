from django.contrib import admin
from university.models import *

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['id', "first_name", "last_name"]}),
        ("Birth Date information", {"fields": ["birth_date"]}),
        ("Study group info", {"fields": ["study_group"]}),
    ]
    list_display = ["first_name", "last_name", "birth_date", "study_group"]
    list_filter = ["birth_date", "study_group"]
    search_fields = ["last_name"]

class ScheduleAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['id', 'student', 'discipline', 'room']}),
                 ('Time of lesson', {'fields': ['start_time', 'end_time']}),
                 ('Additional info', {'fields': ['lesson_type']})]
    list_display = ['start_time', 'end_time', 'lesson_type', 'student', 'discipline', 'room']
    list_filter =  ['start_time', 'end_time', 'lesson_type']
    search_fields = ['lesson_type']

admin.site.register(Student, StudentAdmin)
admin.site.register(Discipline)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(StudyGroup)
admin.site.register(Schedule, ScheduleAdmin)
