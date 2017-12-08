# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

import models
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(models.Post)
