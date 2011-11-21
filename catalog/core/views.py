# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings


def home(request):
    return HttpResponse("Ok")
