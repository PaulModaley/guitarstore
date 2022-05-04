from django.db import models
from django.forms import ModelForm

class Newsletter(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 250)
    consent = models.BooleanField(max_length=40)
