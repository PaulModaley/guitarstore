from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.
def profile(request):
    return render(request, 'profile.html', {})

def all_products(request):
    """ A view to show products / searched products /selected category""" 
    products = Product.objects.all()
    query = None
    category = None   

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)                       
            
        if 'category' in request.GET:
            category = request.GET['category']           
            products = products.filter(category__name=category)           

    paginator = Paginator(products, 6) # Show 6 products per page.
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'search': query,
        
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)