# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import smart_str, smart_unicode

from django.db import models
from ..Asignatura.models import Asignatura

# Create your models here.
class Tutor(models.Model):
    idTutor = models.PositiveSmallIntegerField(primary_key = True, null = False, blank = False,)
    nombre = models.CharField(max_length = 200, null = False, blank = False,)
    descripcion = models.CharField(max_length = 500, null = False, blank = False,)
    imagen = models.ImageField(upload_to = 'photos', null = False, blank = False,)
    asignaturas = models.ManyToManyField(Asignatura)

    def __str__(self):
        return smart_str(self.nombre)
