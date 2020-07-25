from product.forms import ProductForm
from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.decorators import login_required



@login_required(login_url="login")
def product_create(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            context["products"] = Product.objects.filter(
                available=True,
                deleted=False
            )
            context["message"] = "Товар был успешно добавлен"
            return render( request ,"product/products.html", context)

    context["form"] = ProductForm()

    return render(
        request,
        "product/form.html",
        context
    )