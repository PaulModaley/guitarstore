from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]