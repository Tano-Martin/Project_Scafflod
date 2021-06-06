from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Category', views.CategoryViewSet)
router.register('Partner', views.PartnerViewSet)
router.register('Project', views.ProjectViewSet)
router.register('PictureProject', views.PictureProjectViewSet)
router.register('Testimonial', views.TestimonialViewSet)
