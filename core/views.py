from django.shortcuts import render,\
    HttpResponse, redirect 

def home(request):
    return redirect("products")


def test(request):
    return HttpResponse("test page")
