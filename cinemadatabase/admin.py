# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from cinemadatabase.models import Film,Actor
# Register your models here.

admin.site.register(Film)
admin.site.register(Actor)
