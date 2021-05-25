from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'title', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Aperçu des images' 

@admin.register(models.OptionAbout)
class OptionAboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ( 'images_view', 'title', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Aperçu des images' 

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name_site', 'location', 'email', 'contact', 'copyrights', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']


@admin.register(models.SocialIcon)
class SocialIconAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'link', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'name', 'poste', 'twitter', 'facebook', 'linkedin', 'instagram', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Aperçu des images'
