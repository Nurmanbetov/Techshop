from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product.models import Product


@login_required(login_url='/login/')
def product_delete(request, id):
    product = Product.objects.get(id=id)
    context = {}

    if product.user != request.user:
        context["message"] = "У вас нет доступа!"
    else:
        product.deleted = True
        product.save()
        context["message"] = "Товар был удален"

    context["type"] = "danger"
    return render(request, "core/message.html", context)
