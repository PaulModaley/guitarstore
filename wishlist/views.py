from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from products.models import Product

# Create your views here.

def wishlist(request):
    """ A view that renders the cart contents page """

    return render(request, 'wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

