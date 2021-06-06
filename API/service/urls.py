from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Service', views.ServiceViewSet)
router.register('Faq', views.FaqViewSet)
router.register('Prestation', views.PrestationViewSet)
router.register('Pack', views.PackViewSet)
router.register('Advantage', views.AdvantageViewSet)