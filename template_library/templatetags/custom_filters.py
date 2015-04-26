from django import template
import os
import publication_base.settings as settings

register = template.Library()

@register.filter
def divide(value, arg):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    The usage is like:
        {{ var|div:2 }}
    '''
    try:
        value = int(value)
        arg = int(arg)
        if arg:
            return value / arg
    except:
        pass
    return ''

@register.filter
def get_edition_cover(value):
    '''
    returns the jpg file called <value>.jpg or default file
    if jpg does not exist
    '''
    try:
        name_without_ext, ext = os.path.splitext(value)
        jpg_file = name_without_ext + ".jpg"
        path_to_jpg = os.path.join(settings.MEDIA_ROOT, "covers")
        full_path = os.path.join(path_to_jpg, jpg_file)
        if os.path.isfile(full_path):
            return "covers/" + jpg_file
        return "covers/default.jpg"
    except:
        pass

    return ''
