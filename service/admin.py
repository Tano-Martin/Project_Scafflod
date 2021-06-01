from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'description', 'color', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']


@admin.register(models.Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

@admin.register(models.Prestation)
class PrestationAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'title', 'description', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Aperçu des images'

@admin.register(models.Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'period', 'marque', 'title_marque', 'activate', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    filter_horizontal = ('advantage', )
    list_editable = ['status']

@admin.register(models.Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_activate', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
