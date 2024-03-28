from django import template

register = template.Library()


@register.filter(name='any_digit')
def for_renge(number):
    return (number - int(number)) > 0
