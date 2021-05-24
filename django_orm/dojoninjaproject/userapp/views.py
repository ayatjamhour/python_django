from django.shortcuts import  render ,redirect
from . import models 
from .models import *

#from django.contrib import messages

def alldojo(request):
    context = {
        'all_dojo' : models.all_dojo()
        # 'all_ninja' : models.all_ninja()
    }
    return render(request,"index.html" , context)

def add_dojo(request):
    dojo.objects.create(
        name=request.POST["name"] ,
        city=request.POST["city"] ,
        state=request.POST["state"] ,
    )
    return redirect("/")
 
def add_ninja (request):
    # errors= ninja.objects.basic_validator(request.POST)
    # if len(errors) > 0:
    #     for error in errors.value():
    #         messages.error(request , error )
    #     return redirect("/")

    selected_dojo = dojo.objects.get(id=request.POST["dojo_id"])
    ninja.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            dojo=selected_dojo,
        )
    return redirect("/")