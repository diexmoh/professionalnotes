# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.list import ListView
from ..Tutor.models import Tutor

# Create your views here.
class ListViewTutor(ListView):
    model = Tutor
    template_name = 'tutor.html'
    context_object_name = 'tutores'
