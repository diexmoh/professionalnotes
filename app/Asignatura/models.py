# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import smart_str, smart_unicode

from django.db import models

# Create your models here.
class Asignatura(models.Model):
    idAsignatura = models.PositiveSmallIntegerField(primary_key = True, null = False, blank = False,)
    nombreAsig = models.CharField(max_length = 50, null = False, blank = False,)
    descripcion = models.CharField(max_length = 255, null = False, blank = False,)

    def __str__(self):
        return smart_str(self.nombreAsig)
