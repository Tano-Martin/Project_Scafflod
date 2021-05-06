from django.shortcuts import render, get_object_or_404
from . import models
from portfolio import models as models_portfolio


def index(request):
    banner = models.Banner.objects.filter(status=True).first()
    projets = models_portfolio.Project.objects.filter(status=True)
    cartegories = models_portfolio.Category.objects.filter(status=True)
    websites = models.Website.objects.filter(status=True)
    partners = models_portfolio.Partner.objects.filter(status=True)
    teams = models.Team.objects.filter(status=True)
    return render(request, "index.html", locals())



def portfolio(request, id):
    projet = get_object_or_404(models_portfolio.Project, id=id)
    return render(request, "portfolio-details.html", locals())
