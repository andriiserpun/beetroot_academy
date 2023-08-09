import datetime
from django import template

register = template.Library()

@register.filter
def format_dt(dt: datetime.datetime) -> str:
    return dt.strftime("%H:%M %d.%m.%Y")
