from django import forms
from django.db import models
from .models import NewsletterSubscribe

class NewsletterSubscribe(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [ 
            'email',
        ]
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control'}),
        }