from django import template

register = template.Library()


@register.filter(name='is_active')
def filter_is_active(queryset):
    return queryset.filter(is_active=True)
