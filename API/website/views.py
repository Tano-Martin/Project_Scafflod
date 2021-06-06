from rest_framework import viewsets
from . import serializers
from website import models


class AboutViewSet(viewsets.ModelViewSet) :
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

class OptionAboutViewSet(viewsets.ModelViewSet) :
    queryset = models.OptionAbout.objects.all()
    serializer_class = serializers.OptionAboutSerializer

class BannerViewSet(viewsets.ModelViewSet) :
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer

class ContactViewSet(viewsets.ModelViewSet) :
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

class NewsletterViewSet(viewsets.ModelViewSet) :
    queryset = models.Newsletter.objects.all()
    serializer_class = serializers.NewsletterSerializer

class WebsiteViewSet(viewsets.ModelViewSet) :
    queryset = models.Website.objects.all()
    serializer_class = serializers.WebsiteSerializer

class SocialIconViewSet(viewsets.ModelViewSet) :
    queryset = models.SocialIcon.objects.all()
    serializer_class = serializers.SocialIconSerializer

class TeamViewSet(viewsets.ModelViewSet) :
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
