from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import UserWishlist, WishlistProduct


# Create your views here.

def wishlist(request):
    """ A view that renders the wishlist page """

    return render(request, 'wishlist.html')

class ShowWishlist(View):

    def get(self, request):
        wishlists = UserWishlist.objects.filter(wishlist_owner=request.user.id).all()
        # wishlist_products = WishlistProduct.objects.filter(wishlist=wishlists).all()
        context = {
            'wishlists': wishlists
        }
        
        return render(request, 'wishlist.html', context)



