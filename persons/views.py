from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Kebaktian, Kelas, Members, MemberTypes
from .serializer import KebaktianSerializer, KelasSerializer, MemberTypesSerializer, MembersSerializer

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
def membertypes_list(request):
	if request.method == 'GET':
		membertypes = MemberTypes.objects.all()
		serializer = MemberTypesSerializer(membertypes, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = MemberTypesSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def membertypes_detail(request, pk):
	try:
		membertypes = MemberTypes.objects.get(pk=pk)
	except MemberTypes.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = MemberTypesSerializer(membertypes)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = MemberTypesSerializer(membertypes, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		membertypes.delete()
		return HttpResponse(status=204)

@csrf_exempt
def members_list(request):
	if request.method == 'GET':
		members = Members.objects.all()
		serializer = MembersSerializer(members, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = MembersSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def members_detail(request, pk):
	try:
		members = Members.objects.get(pk=pk)
	except Members.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = MembersSerializer(members)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = MembersSerializer(members, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		members.delete()
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

@csrf_exempt
def member_login(request):
	data = JSONParser().parse(request)
	mobilenumber = data["mobilenumber"]
	return HttpResponse(status=200)