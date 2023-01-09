from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from main.models import *
import sweetify


def verified_or_superuser(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        profile = request.user
        if profile.verified or profile.is_superuser:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('verify'))

  return wrap



