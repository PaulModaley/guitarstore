from django.urls import path
from . import views
from .forms import NewsletterSubscribe
from .views import subscribe
from .models import Subscription


urlpatterns = [
    path('subscribe/',
         views.subscribe, name='subscribe'),
]