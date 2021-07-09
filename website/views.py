import json
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from . import models
from .forms import ContactForm, NewsletterForm
from portfolio import models as models_portfolio
from service import models as models_service
from django.views.decorators.csrf import csrf_exempt



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
    return render(request, "index.html", locals())

def portfolio(request, id):
    website = models.Website.objects.filter(status=True).first()
    projet = models_portfolio.Project.objects.get(id=id)
    return render(request, "portfolio-details.html", locals())

#formulaire
def is_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False

def contactPost(request):        
    if request.method == 'POST':
        formCont = ContactForm(request.POST)
        if formCont.is_valid():
            formCont.save()
        return redirect('index')
    else :
        formCont = ContactForm()
        return redirect('index')

@csrf_exempt
def newsletterPost(request):
    message = ""
    success = False
    if request.method == 'POST':
        newEmail = json.loads(request.POST.get('email'))
        if newEmail.isspace():
            message = "Veuillez remplir ce champs avant de le soumettre !"
        elif is_email(newEmail):
            message = "Email invalide"
        else:
            news, created = models.Newsletter.objects.get_or_create(email=newEmail)
            news.save()
            if created:
                message = "Email envoyé avec succès"
            else:
                message = "Email déjà envoyé"
            success = True
    datas = {
        "success": success,
        "message": message
    }
    return JsonResponse(datas, safe=False)
