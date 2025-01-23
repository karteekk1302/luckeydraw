from django import template

register = template.Library()

@register.filter
def is_dict(value):
    return isinstance(value, dict)

@register.filter
def is_string(value):
    return isinstance(value, str)