from django.shortcuts import render
from .forms import Add_Subscriber
from .models import Newsletter

# Create your views here.
def add_subscriber(request):
    form = Add_Subscriber
    return render(request, 'newslettter/add_subscriber')