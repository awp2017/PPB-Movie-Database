# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from taskmanager.models import Group, Task
# Register your models here.

admin.site.register(Group)
admin.site.register(Task)
