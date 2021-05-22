from django.shortcuts import render,redirect
from .models import User
from . import models
# Create your views here.
def index(request):
    context ={
        "Allusers":User.objects.all()
    }
    return render(request, 'index.html',context)

def new(request):
    if request.method == "POST":
        first=request.POST["First"]
        User.objects.create(first_name=first , last_name=request.POST["Last"],email=request.POST["Email"],age=request.POST["Age"])
    return redirect("/")