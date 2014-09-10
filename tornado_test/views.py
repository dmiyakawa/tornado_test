from django.http import HttpResponse
import django.core.handlers.wsgi

import django
import os
import sys

def home(request):
    version = ('Python: {}\nDjango: {}\n'
               .format(sys.version.replace('\n', ' '),
                       django.get_version()))
    return HttpResponse(version, content_type="text/plain")
