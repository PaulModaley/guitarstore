# from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.contrib import messages
# from django.db.models import Q
# from django.db.models.functions import Lower
# from django.shortcuts import get_object_or_404, render, HttpResponse
# from django.views import View
# from .models import UserWishlist, WishlistProduct
# from products.models import *
# from django.contrib.auth.decorators import login_required


# # Create your views here.

# def wishlist(request):
#     """ A view that renders the wishlist page """

#     return render(request, 'wishlist.html')


# class ShowWishlist(View):

#     def get(self, request):
#         _wishlists = []
#         wishlists = UserWishlist.objects.filter(wishlist_owner=request.user.id).all()
#         for wishlist in wishlists:
#             wishlist_products = WishlistProduct.objects.filter(
#                 wishlist=wishlist.id
#             ).all()
#             _wishlists.append({
#                 "wishlist_name": wishlist.wishlist_name,
#                 "wishlist_owner": wishlist.wishlist_owner,
#                 "products": wishlist_products
#             })
#         context = {
#             'wishlists': _wishlists
#         }
        
#         return render(request, 'wishlist.html', context)

# @login_required
# def add_to_wishlist(request, product_id):
#     print("I am here")
#     if request.method == "POST":
#         print(request.POST)
#         #Handle data
#         wishlist_name = request.POST["Wish List Name"]
#         product = request.POST["Product"]
#         wishlist = UserWishlist.objects.filter(user=request.user).first()
#         if wishlist:
#             wishlist.wishlist_name = wishlist_name
#             wishlist.product = product
#             profile.save()
            
#         else:
#             UserWishlist(
#                 wishlist_name==request.wishlist_name,
#             ).save()
#         context = {
#             "Wish List Name": wishlist_name,
#         }
        
#         return render(request, 'wishlist.html', context)
        
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import WishList


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishList.objects.filter(user_profile=user)

    template = 'wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """
    View to add products to wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    WishList.objects.create(
        user_profile=user,
        product=product
    )
    messages.info(
        request, f'{product.name} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, product_id):
    """
    View to remove products from wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    # get the product to be removed from WishList
    product = get_object_or_404(Product, pk=product_id)
    # find a match to the product and user, then .delete() it
    WishList.objects.filter(product=product, user_profile=user).delete()

    messages.info(request,
                  f'{product.name} has been removed from your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))