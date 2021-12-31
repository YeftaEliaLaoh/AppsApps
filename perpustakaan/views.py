from django.db.models import F
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializer import BooksSerializer, BookCategorySerializer
from .models import Books, BookCategory

class BooksCreateApi(generics.CreateAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

class BooksApi(generics.ListAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

class BooksUpdateApi(generics.RetrieveUpdateAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

class BooksDeleteApi(generics.DestroyAPIView):
	queryset = Books.objects.all()
	serializer_class = BooksSerializer

@csrf_exempt
def bookCategory_list(request):
	"""
	List all code bookCategory, or create a new bookCategory.
	"""
	if request.method == 'GET':
		bookCategory = BookCategory.objects.all()
		serializer = BookCategorySerializer(bookCategory, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = BookCategorySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def bookCategory_detail(request, pk):
	"""
	Retrieve, update or delete a code bookCategory.
	"""
	try:
		bookCategory = BookCategory.objects.get(pk=pk)
	except BookCategory.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = BookCategorySerializer(bookCategory)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = BookCategorySerializer(bookCategory, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		bookCategory.delete()
		return HttpResponse(status=204)
	
def retrieveall(request):
	books = Books.objects.all().select_related("idbookcategory").values(useruid=F("idbookcategory__name"),seruid=F("name"))
	print(str(books.query))
	#qs_json = serializers.serialize('json', books)
	return HttpResponse(books, content_type='application/json')