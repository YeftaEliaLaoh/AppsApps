from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

class Kebaktian(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

class Kelas(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

class Roles(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']

class Users(AbstractUser):
    roleid = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)
    kelasId = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)
    kebaktianId = models.ForeignKey(Kebaktian, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    postcode = models.CharField(max_length=8)
    mobilenumber = models.CharField(max_length=10, unique=True)

class UserSubmissions(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    updatedby = models.CharField(max_length=10)
    approveddate = models.DateField(null=True, blank=True)
    canceldate = models.DateField(null=True, blank=True)
    createddate = models.DateField(default=now)
    deleteddate = models.DateField(null=True, blank=True)