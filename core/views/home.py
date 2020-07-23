from django.shortcuts import redirect



def home(request):
    print("------------")
    print("Пользователь:")
    print(request.user)
    print("------------")
    return redirect("products")