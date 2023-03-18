from django import template

register = template.Library()


@register.filter(name='is_recommended')
def is_recommended(scholarship, user):
    if user.is_authenticated and user.profile:
        if user.profile.education >= scholarship.education_level:
            return True
    return False
