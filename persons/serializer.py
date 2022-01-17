from rest_framework import  serializers
from .models import Kebaktian, Kelas, Roles, Users

class KebaktianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kebaktian
        fields = '__all__'

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__'

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'