from django.db import models
from django.utils import timezone


class KeepApp(models.Model):
    title = models.CharField(max_length=100, default='', blank=False)
    status = models.BooleanField(default=False)
    due_date = models.DateField(default=timezone.now())
