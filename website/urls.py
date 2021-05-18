from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, portfolio, newletterpost


urlpatterns = [
    path('', index, name="index"),
    path('details/<int:id>/', portfolio, name="detail"),  
    path("newletter-post/",  newletterpost, name="newletter_post")  
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)