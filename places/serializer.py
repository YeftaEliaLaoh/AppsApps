from rest_framework import  serializers
from .models import Gereja

class GerejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gereja
        fields = '__all__'