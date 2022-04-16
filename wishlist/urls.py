from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowWishlist.as_view(), name='wishlist'),
    path('AddtoWishlist/<int:product_id>/',
         views.AddtoWishlist, name='AddtoWishlist'),
]