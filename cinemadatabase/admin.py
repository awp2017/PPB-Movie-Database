# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from cinemadatabase.models import Film,Actor,Category,Comment,Discussion
# Register your models here.

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Discussion)
