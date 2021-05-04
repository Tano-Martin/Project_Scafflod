from website import models

def my_data(request):
    sociaux = models.SocialIcon.objects.filter(status=True)
    return locals()
