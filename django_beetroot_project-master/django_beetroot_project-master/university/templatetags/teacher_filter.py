from django import template
import random

register = template.Library()

@register.simple_tag
def generate_email(first_name, last_name, id_):
    rand_int = random.choice(range(1,9999))
    final_id = rand_int * id_ % 1000
    return f"{first_name}_{last_name}{final_id}@university.com"

@register.filter
def print_disciplines(disciplines):
    count_disciplines = disciplines.count()
    if count_disciplines == 0:
        return "The teacher doesn't have disciplines"
    elif count_disciplines == 1:
        return f"The teacher has one discipline: {disciplines.first().get_discipline_name_display()}"
    else:
        discipline_list = [discipline.get_discipline_name_display() for discipline in disciplines]
        discipline_names = ", ".join(discipline_list)
        return f"The teacher has {count_disciplines} disciplines: {discipline_names}"