from django import template
register = template.Library()

@register.filter()
def my_len(value):
    return len(value)