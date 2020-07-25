from django.shortcuts import render
from django.db.models import Q
from product.models import Product


def products(request):
    context = {}
    if "query" in request.GET:
        word = request.GET.get("query")
        context["products"] = Product.objects.filter(
            Q(available=True),
            Q(deleted=False),
            Q(name__contains=word) |
            Q(description__contains=word) |
            Q(category__name__contains=word)
        )
    else:
        context["products"] = Product.objects.filter(
            available=True,
            deleted=False
        )
    return render(request, "product/products.html", context)
