from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


class Roles(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']

class Users(AbstractUser):
    roleid = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)
    birthdate = models.DateField(null=True, blank=True)
    mobilenumber = models.CharField(max_length=10, unique=True)

class UserSubmissions(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    updatedby = models.CharField(max_length=10)
    approveddate = models.DateField(null=True, blank=True)
    canceldate = models.DateField(null=True, blank=True)
    createddate = models.DateField(default=now)
    deleteddate = models.DateField(null=True, blank=True)