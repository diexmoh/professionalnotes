# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ..Asignatura.models import Asignatura

# Register your models here.
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    pass
