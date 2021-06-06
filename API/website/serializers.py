from rest_framework import serializers
from website import models

class AboutSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.About
        fields = '__all__'
    
class OptionAboutSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.OptionAbout
        fields = '__all__'

class BannerSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Banner
        fields = '__all__'

class ContactSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Contact
        fields = '__all__'

class NewsletterSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Newsletter
        fields = '__all__'

class WebsiteSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Website
        fields = '__all__'

class SocialIconSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.SocialIcon
        fields = '__all__'

class TeamSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = models.Team
        fields = '__all__'