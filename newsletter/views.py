from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import Subscribe
from .models import Subscribe

from django.shortcuts import render
# Create your views here.
def newsletter(request):
    """ A view to return the index page """

    return render(request, 'newsletter/newsletter.html')