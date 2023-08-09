from university.models import *

delete_teacher = Teacher.objects.get(id=1)
delete_teacher.delete()

delete_student = Student.objects.get(id=2)
delete_student.delete()

discipline_full_name = Discipline.objects.get(id=5)
discipline_full_name.get_discipline_name_display()

update_teacher = Teacher.objects.get(first_name='Sophia', last_name="Taylor")
update_teacher.last_name = "Johnson"
update_teacher.save()