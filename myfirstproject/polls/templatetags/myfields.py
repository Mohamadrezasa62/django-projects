from django import template

register = template.Library()


@register.filter(name='lower_me')
def lower_me(value: str):
    return value.lower()
