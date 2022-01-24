from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Location
from .serializer import LocationSerializer

@csrf_exempt
def location_list(request):
	if request.method == 'GET':
		location = Location.objects.all()
		serializer = LocationSerializer(location, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = LocationSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def location_detail(request, pk):
	try:
		location = Location.objects.get(pk=pk)
	except Location.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = LocationSerializer(location)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = LocationSerializer(location, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		location.delete()
		return HttpResponse(status=204)
