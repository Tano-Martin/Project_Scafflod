from django.shortcuts import render, get_object_or_404
from . import models
from portfolio import models as models_portfolio
from service import models as models_service


def index(request):
    banner = models.Banner.objects.filter(status=True).first()
    projets = models_portfolio.Project.objects.filter(status=True)
    cartegories = models_portfolio.Category.objects.filter(status=True)
    website = models.Website.objects.filter(status=True).first()
    partners = models_portfolio.Partner.objects.filter(status=True)
    teams = models.Team.objects.filter(status=True)
    about = models.About.objects.filter(status=True).first()
    optionabouts = models.OptionAbout.objects.filter(status=True)
    services = models_service.Service.objects.filter(status=True)
    faqs = models_service.Faq.objects.filter(status=True)
    testimonials = models_portfolio.Testimonial.objects.filter(status=True)
    return render(request, "index.html", locals())


def portfolio(request, id):
    projet = get_object_or_404(models_portfolio.Project, id=id)
    return render(request, "portfolio-details.html", locals())
