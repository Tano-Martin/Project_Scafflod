from .models import Contact
from django.forms import ModelForm, fields

class ContactForm(ModelForm):
    class Meta: # une classe qui utilise des classes
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

