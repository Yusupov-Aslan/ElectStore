import json

from django import template

register = template.Library()


@register.simple_tag
def ratio(num1, num2, num3):
    return round(float(num1) * float(num2) / float(num3), 2)


@register.filter
def str_to_json(data):
    return json.loads(data)
