from jalali_date import datetime2jalali
from django import template
register = template.Library()


@register.filter(name='show_jalali')
def show_jalali(value):
    return datetime2jalali(value).strftime('سال : %Y ماه: %m روز: %d' + 'ساعت: %H:%M:%S')
