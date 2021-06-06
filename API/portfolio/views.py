from rest_framework import viewsets
from . import serializers
from portfolio import models

class CategoryViewSet(viewsets.ModelViewSet) :
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class PartnerViewSet(viewsets.ModelViewSet) :
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer

class ProjectViewSet(viewsets.ModelViewSet) :
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

class PictureProjectViewSet(viewsets.ModelViewSet) :
    queryset = models.PictureProject.objects.all()
    serializer_class = serializers.PictureProjectSerializer

class TestimonialViewSet(viewsets.ModelViewSet) :
    queryset = models.Testimonial.objects.all()
    serializer_class = serializers.TestimonialSerializer

# class ViewSet(viewsets.ModelViewSet) :
#     queryset = .objects.all()
#     serializer_class = serializers.serializers

