# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def truncate_words(value, num_words):
    words = value.split()[:num_words]
    return ' '.join(words) + ('...' if len(value.split()) > num_words else '')


@register.filter
def split(value,delimiter):
    return value.split(delimiter)