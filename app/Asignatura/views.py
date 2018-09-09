# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.list import ListView
from ..Asignatura.models import Asignatura

# Create your views here.
class ListViewAsignatura(ListView):
    model = Aignatura
    template_name = 'asignatura.html'
    context_object_name = 'asignaturas'
