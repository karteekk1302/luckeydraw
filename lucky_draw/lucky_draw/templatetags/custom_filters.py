from django import template

register = template.Library()

@register.filter
def is_dict(value):
    return isinstance(value, dict)

@register.filter
def is_string(value):
    return isinstance(value, str)

@register.filter
def get_resultvalue(result, key):
    if result and isinstance(result, dict):
        return result.get(key, 0)  # Using dict.get() with default value
    return 0