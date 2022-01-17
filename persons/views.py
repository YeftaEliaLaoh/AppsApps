from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Kebaktian, Kelas, Users, Roles
from .serializer import KebaktianSerializer, KelasSerializer, RolesSerializer, UsersSerializer

@csrf_exempt
def kebaktian_list(request):
	if request.method == 'GET':
		kebaktian = Kebaktian.objects.all()
		serializer = KebaktianSerializer(kebaktian, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = KebaktianSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def kebaktian_detail(request, pk):
	try:
		kebaktian = Kebaktian.objects.get(pk=pk)
	except Kebaktian.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = KebaktianSerializer(kebaktian)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = KebaktianSerializer(kebaktian, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		kebaktian.delete()
		return HttpResponse(status=204)

@csrf_exempt
def kelas_list(request):
	if request.method == 'GET':
		kelas = Kelas.objects.all()
		serializer = KelasSerializer(kelas, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = KelasSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def kelas_detail(request, pk):
	try:
		kelas = Kelas.objects.get(pk=pk)
	except Kelas.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = KelasSerializer(kelas)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = KelasSerializer(kelas, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		kelas.delete()
		return HttpResponse(status=204)

@csrf_exempt
def roles_list(request):
	if request.method == 'GET':
		roles = Roles.objects.all()
		serializer = RolesSerializer(roles, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = RolesSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def roles_detail(request, pk):
	try:
		roles = Roles.objects.get(pk=pk)
	except Roles.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = RolesSerializer(roles)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = RolesSerializer(roles, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		roles.delete()
		return HttpResponse(status=204)

@csrf_exempt
def users_list(request):
	if request.method == 'GET':
		publisher = Users.objects.all()
		serializer = UsersSerializer(publisher, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = UsersSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def users_detail(request, pk):
	try:
		language = Users.objects.get(pk=pk)
	except Users.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = UsersSerializer(language)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = UsersSerializer(language, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		language.delete()
		return HttpResponse(status=204)

@csrf_exempt
def user_login(request):
	data = JSONParser().parse(request)
	username = data["username"]
	password = data["password"]
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponse(status=200)

	else:
		return HttpResponse(status=403)

@csrf_exempt
def user_logout(request):
	logout(request)
	return HttpResponse(status=200)