from django.db import models
from django.utils.timezone import now

class Kebaktian(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

class Kelas(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

class MemberTypes(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']

class Members(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    membertypeid = models.ForeignKey(MemberTypes, on_delete=models.CASCADE, null=True)
    kelasId = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)
    kebaktianId = models.ForeignKey(Kebaktian, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    #postcode = models.CharField(max_length=8, default='')
    mobilenumber = models.CharField(max_length=13, unique=True)

class MemberSubmissions(models.Model):
    memberid = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
    updatedby = models.CharField(max_length=10)
    approveddate = models.DateField(null=True, blank=True)
    canceldate = models.DateField(null=True, blank=True)
    createddate = models.DateField(default=now)
    deleteddate = models.DateField(null=True, blank=True)