from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:id>/', views.portfolio, name="detail"),  
    path("newsletterPost/",  views.newsletterPost, name="newsletterPost"),
    path("contactPost/",  views.contactPost, name="contactPost"), 
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)