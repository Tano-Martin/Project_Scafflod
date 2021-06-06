from rest_framework import serializers
from service import models

class ServiceSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Service
        fields = '__all__'

class FaqSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Faq
        fields = '__all__'

class PrestationSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Prestation
        fields = '__all__'

class PackSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Pack
        fields = '__all__'

class AdvantageSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Advantage
        fields = '__all__'