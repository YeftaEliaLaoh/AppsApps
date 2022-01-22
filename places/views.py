from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Gereja
from .serializer import GerejaSerializer

@csrf_exempt
def gereja_list(request):
	if request.method == 'GET':
		gereja = Gereja.objects.all()
		serializer = GerejaSerializer(gereja, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = GerejaSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def kebaktian_detail(request, pk):
	try:
		gereja = Gereja.objects.get(pk=pk)
	except Gereja.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = GerejaSerializer(gereja)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = GerejaSerializer(gereja, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		gereja.delete()
		return HttpResponse(status=204)
