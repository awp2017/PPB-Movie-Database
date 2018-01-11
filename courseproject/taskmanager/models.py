# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=200)
    public = models.BooleanField(default=False)
    
    responsible = models.ForeignKey(User, null=True, blank=True)
    users = models.ManyToManyField(User, blank=True, 
                                   related_name="task_groups")

    def __str__(self):
        return self.name
        
class Ceva(models.Model):


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    deadline = models.DateTimeField(null=True, blank=True)
    category = models.IntegerField(choices=[
            (1, "Mandatory"),
            (2, "Nice to have"),
            (3, "Urgent"),
            (4, "Extra points"),
        ]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    group = models.ForeignKey(Group)
    responsible = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title
