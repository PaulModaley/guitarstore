from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views import View
from .models import UserWishlist, WishlistProduct
from products.models import *


# Create your views here.

def wishlist(request):
    """ A view that renders the wishlist page """

    return render(request, 'wishlist.html')



class ShowWishlist(View):

    def get(self, request):
        _wishlists = []
        wishlists = UserWishlist.objects.filter(wishlist_owner=request.user.id).all()
        for wishlist in wishlists:
            wishlist_products = WishlistProduct.objects.filter(
                wishlist=wishlist.id
            ).all()
            _wishlists.append({
                "wishlist_name": wishlist.wishlist_name,
                "wishlist_owner": wishlist.wishlist_owner,
                "products": wishlist_products
            })
        context = {
            'wishlists': _wishlists
        }
        
        return render(request, 'wishlist.html', context)


def add_to_wishlist(request, product_id):
    print("I am here")
    if request.method == "POST":
        print(request.POST)
        #Handle data
        wishlist_name = request.POST["Wish List Name"]
        product = request.POST["Product"]
        wishlist = UserWishlist.objects.filter(user=request.user).first()
        if wishlist:
            wishlist.wishlist_name = wishlist_name
            wishlist.product = product
            profile.save()
            
        else:
            UserWishlist(
                wishlist_name==request.wishlist_name,
            ).save()
        context = {
            "Wish List Name": wishlist_name,
        }
        
        return render(request, 'wishlist.html', context)
        
