# -*- coding: utf-8 -*-

from django.conf import settings  # import the settings file
from thumbnail import is_python_magick

def application_parms(request):
    # return the value you want as a dictionary. you may add multiple values in there.

    return {
            'IS_PYTHON_MAGICK': is_python_magick(),
           }

