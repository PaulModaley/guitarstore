from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ko7AHHeYwWa7liY3QKjZ319f0mIyhVamdn2oDvTqFidVEgFN14cnV36mwVVtzt7698DlhIdv4KJ5sdUNnaqInvf00gsdUpY4R',
        'client_secret': 'sk_test_51Ko7AHHeYwWa7liYtIpy2e81Pp9759wlyfwEP5m0IUhTX8uw5ELkvXtBbj0PAgk7vle8scoC69gjareAA3vIqGWg00ocSR7R5N',
    }

    return render(request, template, context)