from rest_framework.response import Response
from .models import Users
from rest_framework.decorators import api_view
from .serializer import UsersSerializer

@api_view(['GET'])
def users_list(request):
    user_data = Users.objects.all()
    serializer = UsersSerializer(user_data, many=True)
    return Response(serializer.data, status=200)