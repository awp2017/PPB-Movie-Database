# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
# class Url(models.Model):
#     source = models.CharField(max_length=500)
    
#     def __str__(self):
#         return self.source

class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=2000)
    age = models.IntegerField(default=0)
    image = models.FileField(upload_to="actors", default='/media/sample.jpg')
    
    def __str__(self):
        return self.name
    
class Film(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.CharField(max_length=1000)
    cast = models.ManyToManyField(Actor)
    image = models.FileField(upload_to="films", default='/media/sample.jpg')
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name
        
class Discussion(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    id_user = models.ForeignKey(User)
    id_film = models.ForeignKey(Film)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
	text = models.CharField(max_length=1000)
	created_date = models.DateTimeField(default=timezone.now)
	id_user = models.ForeignKey(User)
	id_discussion = models.ForeignKey(Discussion)
	
	def __str__(self):
	    return "a comment"