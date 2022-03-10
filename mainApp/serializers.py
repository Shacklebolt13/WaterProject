from rest_framework.serializers import ModelSerializer
from .models import WaterModel

class WaterModelSerializer(ModelSerializer):
    class Meta:
        model = WaterModel
        fields = '__all__'