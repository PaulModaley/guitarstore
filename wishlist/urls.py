from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowWishlist.as_view(), name='wishlist'),
    # path('', views.wishlist, name='wishlist'),
]