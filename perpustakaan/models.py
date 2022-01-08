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
    barcode = models.CharField(max_length=255)
    kodelama = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    titleseries = models.CharField(max_length=255)
    author1 = models.CharField(max_length=255)
    author2 = models.CharField(max_length=255)
    author3 = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    page = models.IntegerField(null=True)
    yearpurchased = models.CharField(max_length=255)
 #   dateenter = models.DateTimeField(null=True)
    datepublish = models.DateTimeField(null=True)
    rack = models.CharField(max_length=30)
    isrented = models.BooleanField(default=False)
    beingrented = models.BooleanField(default=False)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']

class BookSubmissions(models.Model):
    bookid = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    personid = models.ForeignKey('persons.users', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True, blank=True)
    approveddate = models.DateField(null=True, blank=True)
    canceldate = models.DateField(null=True, blank=True)
    createddate = models.DateField(null=True, blank=True)
    returndate = models.DateField(null=True, blank=True)
    updatedby = models.CharField(max_length=10)