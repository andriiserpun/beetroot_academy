from university.models import *
from django.db.models import Q, Max, Min, Avg

Teacher.objects.filter(id__gt=3)
Teacher.objects.filter(id__gte=3)
Teacher.objects.filter(id__gte=9).update(last_name="AAA")

Teacher.objects.filter(Q(first_name='Daniel') | Q(last_name="AAA"))

Teacher.objects.exclude(id__gte=9)

Teacher.objects.filter(first_name__contains="i").exclude(id__gte=5)

max_salary_result = Teacher.objects.aggregate(max_salary=Max('salary'))
min_salary_result = Teacher.objects.aggregate(min_salary=Min('salary'))
avg_salary_result = Teacher.objects.aggregate(avg_salary=Avg('salary'))
teacher_max_min_info = Teacher.objects.filter(Q(salary=max_salary_result['max_salary']) | Q(salary=min_salary_result['min_salary']))

query_set_teachers = Teacher.objects.filter(id__gte=6)
max_salary_result = query_set_teachers.aggregate(max_salary=Max('salary'))
min_salary_result = query_set_teachers.aggregate(min_salary=Min('salary'))
teacher_max_min_info = query_set_teachers.filter(Q(salary=max_salary_result['max_salary']) | Q(salary=min_salary_result['min_salary']))

teacher_max_min_info.count()
Teacher.objects.count()
