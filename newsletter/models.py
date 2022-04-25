from django import forms
from django.db import models

"""model for form"""


class Subscription(models.Model):
    email = models.EmailField(max_length= 250)