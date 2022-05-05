from django.shortcuts import render
from .forms import Add_Subscriber
from .models import Newsletter
from django.http import HttpResponseRedirect

# Create your views here.
def add_subscriber(request):
    submitted = False
    if request.method == "POST"
    form = Add_Subscriber(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect('/')