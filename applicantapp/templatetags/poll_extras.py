from django import template

register = template.Library()


@register.filter
def favorite(obj, user):
    return obj.is_favorite(user)
