from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Locations
from .serializer import LocationsSerializer

@csrf_exempt
def location_list(request):
	if request.method == 'GET':
		locations = Locations.objects.all()
		serializer = LocationsSerializer(locations, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = LocationsSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def location_detail(request, pk):
	try:
		locations = Locations.objects.get(pk=pk)
	except Locations.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = LocationsSerializer(locations)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = LocationsSerializer(locations, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		locations.delete()
		return HttpResponse(status=204)
