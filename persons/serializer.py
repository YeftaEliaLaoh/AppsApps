from rest_framework import  serializers
from .models import Kebaktian, Kelas, MemberTypes, Members

class KebaktianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kebaktian
        fields = '__all__'

class KelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelas
        fields = '__all__'

class MemberTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberTypes
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'