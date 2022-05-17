from django import template
from new.models import *

register = template.Library()


@register.simple_tag(name='get_tag')
def get_tag():
    return Tag.objects.all()