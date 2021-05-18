from django.shortcuts import redirect, render, get_object_or_404
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
    prestations = models_service.Prestation.objects.filter(status=True)
    avantages = models_service.Advantage.objects.filter(status=True)
    packs = models_service.Pack.objects.filter(status=True)


        #formulaire contact
    if request.method == 'POST':
        formCont = models.Contactform(request.POST)
        if formCont.is_valid():
            formCont.save()
        return redirect('index')
    else :
        formCont = models.Contactform()

    return render(request, "index.html", locals())


def portfolio(request, id):
    website = models.Website.objects.filter(status=True).first()
    projet = get_object_or_404(models_portfolio.Project, id=id)
    return render(request, "portfolio-details.html", locals())

def newletterpost(request):
    newmail = request.POST.get('emailletter')
    new = models.Newletter()
    new.email = newmail
    new.save()
    retour = request.META.get('HTTP_REFERER')
    return redirect(retour, '/')