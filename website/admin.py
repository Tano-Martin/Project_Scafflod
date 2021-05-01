from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('title', 'subtitle', 'picture', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('title', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe('<img src="{obj.image.url}" style="height:50px; width:100px">'.format(url=obj.image.url))

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

@admin.register(models.OptionAbout)
class OptionAboutAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('description', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('description', 'date_add')


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('title', 'description', 'picture', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('title', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe('<img src="{obj.image.url}" style="height:50px; width:100px">'.format(url=obj.image.url))

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name', 'email', 'subject', 'message', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('name', 'date_add')

@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('email', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('email', 'date_add')

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
        #liste des champs a afficher
    list_display = ('name_site', 'description_service', 'description_portfolio', 'call_action', 'description_testimonial', 'description_team', 'description_client', 'description_pricing', 'location', 'email', 'contact', 'maps', 'copyrights', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ['date_add']


@admin.register(models.SocialIcon)
class SocialIconAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('name', 'lien', 'icon', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('name', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe('<img src="{obj.image.url}" style="height:50px; width:100px">'.format(url=obj.image.url))

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('name', 'poste', 'picture', 'twitter', 'facebook', 'linkedin', 'instagram', 'date_add', 'date_update', 'status')

        # Configuration du champ de recherche
    search_fields = ('name', 'date_add')

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe('<img src="{obj.image.url}" style="height:50px; width:100px">'.format(url=obj.image.url))

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin
