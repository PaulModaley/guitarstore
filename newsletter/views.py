from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import Subscriber
from .models import Subscribe

from django.shortcuts import render
# Create your views here.

def newsletter(request):
    form = Subscriber(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return render(request, "newsletter/newsletter.html", context)


# def newsletter(request):

# 	context ={}

# 	# create object of form
# 	form = Subscribe(request.POST or None, request.FILES or None)
	
# 	# check if form data is valid
# 	if form.is_valid():
# 		# save the form data to model
# 		form.save()
# 		messages.success(request, 'Your message has been sent!')
#             # redirect to contact page
        

# 	template = 'newsletter/newsletter.html'