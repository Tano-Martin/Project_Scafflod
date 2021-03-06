from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=255)
    reponse = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

    def __str__(self):
        return self.question

class Prestation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField(upload_to='Prestation_file')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Prestation'
        verbose_name_plural = 'Prestations'

    def __str__(self):
        return self.title

class Pack(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    period = models.CharField(max_length=255)
    marque = models.BooleanField(default=False)
    title_marque = models.CharField(max_length=255, null=True, blank=True)
    activate = models.BooleanField(default=False)
    advantage = models.ManyToManyField("service.Advantage", related_name="advantage_pack")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Pack'
        verbose_name_plural = 'Packs'

    def __str__(self):
        return self.title

class Advantage(models.Model):
    title = models.CharField(max_length=255)
    title_activate = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Advantage'
        verbose_name_plural = 'Advantages'

    def __str__(self):
        return f'{self.title} : active={self.title_activate}'

