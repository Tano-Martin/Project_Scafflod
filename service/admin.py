from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('title', 'icon', 'description', 'color', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('title', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe('<img src="{obj.image.url}" style="height:50px; width:100px">'.format(url=obj.image.url))

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('question', 'reponse', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('question', 'date_add')

@admin.register(models.Benefit)
class BenefitAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('title', 'description', 'picture', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('title', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe('<img src="{obj.image.url}" style="height:50px; width:100px">'.format(url=obj.image.url))

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

