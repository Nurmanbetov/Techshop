from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from core.forms import RegistrationForm




@user_passes_test(user_not_authentiacted)
def registration(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if form.is_valid():
            form.save()
            return redirect("login")
       
    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)