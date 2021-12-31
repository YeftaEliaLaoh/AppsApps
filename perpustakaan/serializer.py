from rest_framework import  serializers
from .models import Books, BookCategory
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        exclude = ('createddate','updateddate')

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ['name']