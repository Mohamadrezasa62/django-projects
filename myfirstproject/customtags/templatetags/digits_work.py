from django import template

register = template.Library()


@register.filter(name='three_digit')
def make_three_digits(value):
    return format(value, ',')
