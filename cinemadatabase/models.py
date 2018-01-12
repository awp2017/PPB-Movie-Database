# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Actor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Film(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    cast = models.ManyToManyField(Actor)
    
    def __str__(self):
        return self.name
