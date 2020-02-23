from django import template

register = template.Library()

@register.inclusion_tag('components/stars.html')
def show_stars(rate, num):
    return {'rate' : rate, 'num': num}