from product.forms import ProductForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product



@login_required(login_url="login")
def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect("home")

    context = {}

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context["product"] = Product.objects.get(id=id)
            context["message"] = "Информация успешно обновлена"
            return render(request, "product/product.html", context)

    
    context["form"] = ProductForm(instance=product)

    return render(
        request,
        "product/form.html",
        context
    )