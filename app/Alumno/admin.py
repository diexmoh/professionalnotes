# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ..Alumno.models import Alumno

# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass
