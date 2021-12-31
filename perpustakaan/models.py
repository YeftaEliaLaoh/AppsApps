from django.db import models
from django.utils.timezone import now

class BookCategory(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']

class Books(models.Model):
    idbookcategory = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    rack = models.CharField(max_length=30)
    isrented = models.BooleanField(default=False)
    beingrented = models.BooleanField(default=False)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']