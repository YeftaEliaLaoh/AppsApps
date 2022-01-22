from django.db import models
from django.utils.timezone import now

class Otp(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)