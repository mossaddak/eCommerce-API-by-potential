from django.shortcuts import render

from productio.models import Product


def PublicProductList(request):
    context = {"products": Product.objects.get_status_fair()[:12]}
    return render(request, "public_products.html", context=context)
