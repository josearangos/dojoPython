# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class idea(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    