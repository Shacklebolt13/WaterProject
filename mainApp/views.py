from django.shortcuts import render
from . import serializers, models
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class WaterModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.WaterModel.objects.all()
    serializer_class = serializers.WaterModelSerializer
