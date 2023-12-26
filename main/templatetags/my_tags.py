from django import template

register = template.Library()


@register.filter()
def my_media(imagine):
    if imagine:
        return f'/media/{imagine}'
    return '/static/image/no_image.jpg'


@register.filter()
def available_filter(val):
    print(val)
    if val:
        return 'В наличии'
    return 'Нет в наличии'
