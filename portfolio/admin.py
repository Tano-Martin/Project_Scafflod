from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']
    
@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'name', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Aperçu des images'

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'client', 'date_project', 'url_project', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

@admin.register(models.PictureProject)
class PictureProjectAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Aperçu des images'

@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('images_view', 'name', 'poste', 'date_add', 'date_update', 'status')
    date_hierarchy = 'date_add'
    list_editable = ['status']

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    images_view.short_description = 'Aperçu des images'

