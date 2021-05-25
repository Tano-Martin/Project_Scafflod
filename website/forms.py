from .models import Newsletter, Contact
from django import forms

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = ['name', 'email', 'subject', 'message']