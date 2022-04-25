from django.shortcuts import render, HttpResponse, redirect
from .models import Subscription
from .forms import NewsletterSubscribe

def subscribe(request):
    form = NewsletterSubscribe(request.POST)
    if form.is_valid():
        form.save()
    print("form submit")

    # else:
    # messages.success(
    # request, 'Thank you for joining our newsletter mailing list')
    
    # print("form submit fail")


    # context = {
    #     'form' : form
    # }


    # return redirect(reverse('subscribe'))