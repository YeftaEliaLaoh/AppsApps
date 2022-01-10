from django.db import models
from django.utils.timezone import now

class Author(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateField(default=now)
    updateddate = models.DateTimeField(null=True)
    
class BookCategory(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']

class Language(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateField(default=now)
    updateddate = models.DateTimeField(null=True)

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    createddate = models.DateField(default=now)
    updateddate = models.DateTimeField(null=True)

class Books(models.Model):
    idbookcategory = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True)
    idlanguage = models.CharField(max_length=255)
    idpublisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    barcode = models.CharField(max_length=255)
    kodelama = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    titleseries = models.CharField(max_length=255)
    page = models.IntegerField(blank=False)
    yearpurchased = models.CharField(max_length=255)
    datepublish = models.DateTimeField(blank=False,default=now)
    rack = models.CharField(max_length=30)
    isrented = models.BooleanField(default=False)
    sellingprice = models.IntegerField(null=True)
    purchaseprice = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    createddate = models.DateTimeField(default=now)
    updateddate = models.DateTimeField(null=True)

    class Meta:
        ordering = ['id']

class BookMappingAuthor(models.Model):
    idbook = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    idauthor = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    createddate = models.DateField(default=now)
    updateddate = models.DateTimeField(null=True)

class BookSubmissions(models.Model):
    idbook = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    personid = models.ForeignKey('persons.users', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    approveddate = models.DateField(null=True)
    canceldate = models.DateField(null=True)
    createddate = models.DateField(default=now)
    returndate = models.DateField(null=True)
    updatedby = models.CharField(max_length=10)
