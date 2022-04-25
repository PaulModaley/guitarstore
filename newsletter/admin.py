from django.contrib import admin
from django.db import models
from .models import Subscription

# Register your models here.
admin.site.site_header = 'Legato Music'

admin.site.register(Subscription)

