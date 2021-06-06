from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('About', views.AboutViewSet)
router.register('OptionAbout', views.OptionAboutViewSet)
router.register('Banner', views.BannerViewSet)
router.register('Contact', views.ContactViewSet)
router.register('Newsletter', views.NewsletterViewSet)
router.register('Website', views.WebsiteViewSet)
router.register('SocialIcon', views.SocialIconViewSet)
router.register('Team', views.TeamViewSet)
