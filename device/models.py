from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class DeviceInfo(models.Model):
    identification = models.CharField(max_length=15)
    url = models.URLField()
    group = models.CharField(max_length=20)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
