from django.shortcuts import redirect, render
from .models import *
def welc(request):
    if 'id' in request.session:
        
        context={
            'user': get_user_cars(request.session["id"]),
            'posts' : messages.objects.all(),
            'comm' : comment.objects.all()
            }
    return render(request,"wall.html",context)
def addpost(request):
    user= get_user_cars(request.session["id"])
    po = request.POST["posting"]
    post_owner=user

    return redirect('/wall')
def addcomm(request,id):
    ow= messages.objects.get(id = id)
    ls =  get_user_cars(request.session["id"])
    cmnt = request.POST['cmnt']
    comment.objects.create(comm=cmnt,postown=ow,userown=ls)
    return redirect('/wall')
