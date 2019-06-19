from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import os.path
from django.http import Http404

# Create your views here.
@login_required
def proxy(request, static_path):
    print('static path: ' + static_path)
    template_path = 'proxy/' + static_path
    print('template_path: ' + template_path)
    print(os.listdir('proxy/templates/proxy'))
    if os.path.isfile('proxy/templates/' + template_path):
        return render(request, template_path)
    else:
        raise Http404("no static site matches the given query.")
