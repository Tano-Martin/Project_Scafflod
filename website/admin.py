from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
        # Liste des champs a afficher
    list_display = ('images_view', 'title', 'subtitle', 'footer', 'date_add', 'date_update', 'status')
    list_display_links = ('images_view', 'title', 'subtitle')

        # Configuration du champ de recherche
    search_fields = ('title', )

    date_hierarchy = 'date_add'

    def images_view(self, obj): #Permet d'avoir un aperçu des images
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:200px">')

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
    list_display = ('title', 'picture', 'date_add', 'date_update', 'status')
    list_display_links = ('picture', 'date_add', 'date_update')
    list_editable = ('title', 'status', )

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
    list_display = ('name_site', 'location', 'email', 'contact', 'copyrights', 'date_add', 'date_update', 'status')

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
