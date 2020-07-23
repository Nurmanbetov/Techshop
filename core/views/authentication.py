from django.contrib.auth.decorators import user_passes_test
from django.contrib import auth 
from .user_not_authentiacted import user_not_authentiacted



@user_passes_test(user_not_authentiacted)
def login(request):
    context = {}
    if "login" in request.POST:
        form = auth.form.AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(home)

    