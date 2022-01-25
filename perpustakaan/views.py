from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .serializer import AuthorSerializer, BookCategorySerializer, LanguagesSerializer, PublisherSerializer,  BooksSerializer
from .models import Author, BookCategory, Languages, Publisher, Books, BookMappingAuthor

@csrf_exempt
def author_list(request):
	if request.method == 'GET':
		author = Author.objects.all()
		serializer = AuthorSerializer(author, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = AuthorSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def author_detail(request, pk):
	try:
		author = Author.objects.get(pk=pk)
	except Author.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = AuthorSerializer(author)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = AuthorSerializer(author, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		author.delete()
		return HttpResponse(status=204)

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

@csrf_exempt
def language_list(request):
	if request.method == 'GET':
		languages = Languages.objects.all()
		serializer = LanguagesSerializer(languages, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = LanguagesSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def language_detail(request, pk):
	try:
		languages = Languages.objects.get(pk=pk)
	except Languages.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = LanguagesSerializer(languages)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = LanguagesSerializer(languages, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		languages.delete()
		return HttpResponse(status=204)

@csrf_exempt
def publisher_list(request):
	if request.method == 'GET':
		publisher = Publisher.objects.all()
		serializer = PublisherSerializer(publisher, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PublisherSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def publisher_detail(request, pk):
	try:
		publisher = Publisher.objects.get(pk=pk)
	except Publisher.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = PublisherSerializer(publisher)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PublisherSerializer(publisher, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		publisher.delete()
		return HttpResponse(status=204)

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

def books_retrieveall(request):
	books = Books.objects.all().select_related("idbookcategory").values(useruid=F("idbookcategory__name"),seruid=F("name"))
	print(str(books.query))
	#qs_json = serializers.serialize('json', books)
	return HttpResponse(books, content_type='application/json')

@api_view(['GET'])
def book_listsubmissions(request,pk):
	books_records=[]
	authors_records=[]

	try:
		book_data = Books.objects.get(pk=pk)
	except Books.DoesNotExist:
		return HttpResponse(status=404)
		
	bookMappingAuthors =  BookMappingAuthor.objects.select_related("idauthor")
	for bookMappingAuthor in bookMappingAuthors:
		eachName = {"name":bookMappingAuthor.idauthor.name}
		authors_records.append(eachName)

	record = {"barcode":book_data.barcode,
				"kodelama":book_data.kodelama,
				"title":book_data.title,
				"titleseries":book_data.titleseries,
				"language":book_data.language,
				"page":book_data.page,
				"yearpurchased":book_data.yearpurchased,
				"datepublish":book_data.datepublish,
				"rack":book_data.rack,
				"isrented":book_data.isrented,
				"beingrented":book_data.beingrented,
				"price":book_data.price,
				"quantity":book_data.quantity,
				"createddate":book_data.createddate.strftime("%d-%m-%Y %H:%M:%S"),
				"updateddate":book_data.updateddate,
				"authors":authors_records}
	books_records.append(record)
	return HttpResponse(books_records, status=200)