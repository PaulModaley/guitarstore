from django import forms
from django.db import models
from .models import NewsletterSubscribe
from django import ModelForm

class NewsletterSubscribe(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = [ 
            'email',
        ]
