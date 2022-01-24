from django.db import models
from django.utils.timezone import now

class Location(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255,null=True)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)
