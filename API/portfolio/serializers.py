from rest_framework import serializers
from portfolio import models

class CategorySerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Category
        fields = '__all__'

class PartnerSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Partner
        fields = '__all__'

class ProjectSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Project
        fields = '__all__'

class PictureProjectSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.PictureProject
        fields = '__all__'

class TestimonialSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Testimonial
        fields = '__all__'
