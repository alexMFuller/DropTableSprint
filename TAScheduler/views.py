from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def myView(request):
    return render(request,"home.html",{})
