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


@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('question', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('question', 'date_add')

@admin.register(models.Prestation)
class PrestationAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ( 'images_view', 'title', 'description', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('title', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:200px">')

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

@admin.register(models.Pack)
class PackAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('title', 'price', 'period', 'marque', 'title_marque', 'activate', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('title', 'date_add')

@admin.register(models.Advantage)
class AdvantageAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('title', 'title_activate', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('title', 'date_add')
