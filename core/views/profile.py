from django.shortcuts import render
from django.contrib.auth.models import User
from core.forms import PasswordChangeForm
from product.models import Product


def profile(request, pk):
    context = {}
    context["user"] = User.objects.get(id=pk)
    context["products"] = Product.objects.filter(user=context["user"])
    context["password_change_form"] = PasswordChangeForm()
    return render(request, "core/profile.html", context)
