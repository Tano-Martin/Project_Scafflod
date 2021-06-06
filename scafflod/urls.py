"""scafflod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from API.portfolio.urls import router as router_portfolio
from API.service.urls import router as router_service
from API.website.urls import router as router_website

router = routers.DefaultRouter()
router.registry.extend(router_portfolio.registry)
router.registry.extend(router_service.registry)
router.registry.extend(router_website.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("website.urls")),
    path('api/', include(router.urls)),
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)