# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ..Tutor.models import Tutor

# Register your models here.
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    pass
