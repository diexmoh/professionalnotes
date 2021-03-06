# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import smart_str, smart_unicode

# Create your models here.
class Alumno(models.Model):
    idAlumno = models.PositiveSmallIntegerField(primary_key = True, null = False, blank = False,)
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    apePat = models.CharField(max_length = 50, null = False, blank = False)
    apeMat = models.CharField(max_length = 50, null = False, blank = False)
    asesorias = models.PositiveSmallIntegerField(null = True, blank = True)
    asesoriaDesc = models.CharField(max_length = 255, null = True, blank = True,)

    def __str__(self):
        return smart_str(self.nombre) + smart_str(self.apePat)
