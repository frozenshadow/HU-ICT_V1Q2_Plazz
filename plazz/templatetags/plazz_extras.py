from django import template
from django.utils.text import slugify

# Initialize the register library
register = template.Library()


@register.filter
def form_friendly(value: str):
    return slugify(value)
