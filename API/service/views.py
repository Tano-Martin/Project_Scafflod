from rest_framework import viewsets
from . import serializers
from service import models

class ServiceViewSet(viewsets.ModelViewSet) :
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class FaqViewSet(viewsets.ModelViewSet) :
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer

class PrestationViewSet(viewsets.ModelViewSet) :
    queryset = models.Prestation.objects.all()
    serializer_class = serializers.PrestationSerializer

class PackViewSet(viewsets.ModelViewSet) :
    queryset = models.Pack.objects.all()
    serializer_class = serializers.PackSerializer

class AdvantageViewSet(viewsets.ModelViewSet) :
    queryset = models.Advantage.objects.all()
    serializer_class = serializers.AdvantageSerializer

