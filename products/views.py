"""product page view"""
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """A view to return the product page
    including sorting and searching queries
    """

    products = Product.objects.all()
    # get all objects from Product model and return context

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    # load products or display a 404 page if not found

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
