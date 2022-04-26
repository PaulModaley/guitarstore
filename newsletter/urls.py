#Based on 

from django.urls import path
from . import views


urlpatterns = [
    path('subscribers', views.subscribers, name='subscribers'),
    path('add_subscriber', views.add_subscriber, name='add_subscriber'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('unsubscribe_registered_user', views.unsubscribe_registered_user,
         name='unsubscribe_registered_user'),
    path('unsubscribe/<int:subscriber_id>/',
         views.unsubscribe_from_email, name='unsubscribe_from_email'),
]