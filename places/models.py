from django.db import models
from django.utils.timezone import now

class Gereja(models.Model):
    name = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)
