from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from products.models import Product

# Create your views here.

def wishlist(request):
    """ A view that renders the cart contents page """

    return render(request, 'wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add a specified product to the wishlist """

    redirect_url = request.POST.get('redirect_url')
    add_to_wishlist = request.session.get('wishlist', {})

    if item_id in add_to_wishlist(wishlist.keys()):
        wishlist[item_id]
        
    request.session['wishlist'] = wishlist
    print(request.session['wishlist'])
    return redirect(redirect_url)


