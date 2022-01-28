from django import template

register = template.Library()


@register.filter
def char_counter(value):
        return chr(96 + value)
