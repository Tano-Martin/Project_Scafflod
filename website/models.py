from django.db import models
from django.forms import ModelForm


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    picture = models.FileField()
    footer = models.TextField(null=True, blank=True)
    option = models.ManyToManyField("website.OptionAbout", related_name="Option_about")

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.title


class OptionAbout(models.Model):
    description = models.CharField(max_length=255)

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'OptionAbout'
        verbose_name_plural = 'OptionAbouts'

    def __str__(self):
        return self.description

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name

class Newletter(models.Model):
    email = models.EmailField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Newletter'
        verbose_name_plural = 'Newletters'

    def __str__(self):
        return self.email

class Website(models.Model):
    name_site = models.CharField(max_length=255)
    description_service = models.TextField()
    description_portfolio = models.TextField()
    call_action = models.TextField()
    description_testimonial = models.TextField()
    description_team = models.TextField()
    description_client = models.TextField()
    description_pricing = models.TextField()
    location = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=255)
    maps = models.TextField()
    copyrights = models.CharField(max_length=255)

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.name_site

class SocialIcon(models.Model):
    name = models.CharField(max_length=255)
    lien = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'SocialIcon'
        verbose_name_plural = 'SocialIcons'

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    picture = models.FileField()
    twitter = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name


    
#formulaire
class Contactform(ModelForm):
    class Meta: # une classe qui utilise des classes
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
