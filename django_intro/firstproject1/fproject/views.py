from django import http
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse

def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/blogs/create")
def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")
def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")
def destroy(request,num):
    return redirect("/blogs")
def json(request ):
    data = {'title':'My first blog',
            'content':'Lorem, ipsum dolor sit amet consectetur adipisicing elit.'
    }
    return JsonResponse(data)

