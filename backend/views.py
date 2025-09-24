from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from . models import Product

def home(request):
    items = Product.objects.all()[:3]
    args = {'items': items}
    return render(request, 'backend/index.html', args)


def contact(request):

    return render(request, 'backend/contact.html')

def shop(request):
    items = Product.objects.all()
    args = {'items': items}
    return render(request, 'backend/shop.html', args)


def add_to_cart(request, product_id):
    # Get product or 404
    product = get_object_or_404(Product, id=product_id)

    # Save product id to session
    cart = request.session.get("cart", [])
    if product_id not in cart:
        cart.append(product_id)
    request.session["cart"] = cart
    request.session.modified = True  # make sure session updates

    return redirect(reverse('backend:cart'))


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", [])
    if product_id in cart:
        cart.remove(product_id)
    request.session["cart"] = cart
    request.session.modified = True
    return redirect(reverse('backend:cart'))



def cart_view(request):
    cart = request.session.get("cart", [])
    total = 0
    products = Product.objects.filter(id__in=cart)
    for i in products:
        total += i.price
    args = {"products": products, 'total': total}
    return render(request, "backend/cart.html", args)


def checkout(request):
    cart = request.session.get("cart", [])
    total = 0
    products = Product.objects.filter(id__in=cart)
    for i in products:
        total += i.price
    args = {"products": products, 'total': total}
    return render(request, "backend/checkout.html", args)






