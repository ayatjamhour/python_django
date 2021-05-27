import contextlib
from typing import ContextManager
from django import http
from django.shortcuts import render, HttpResponse,redirect
from .models import Shows, ShowManager
from django.contrib import messages


def index(request):
    return redirect('/shows')
def add(request):
        # Shows.objects.create(title=request.POST['form_title'],network=request.POST['form_network'],release_date=request.POST['form_res_date'],description=request.POST['form_desc'])
        # context={
        #     'myshows':x,
        # }
        return render(request,'add.html')
def create(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        my_last=Shows.objects.last()
        my_shows_id=my_last.id
        Shows.objects.create(title=request.POST['form_title'],network=request.POST['form_network'],release_date=request.POST['form_res_date'],description=request.POST['form_desc'])
        return redirect('/shows/'+str(my_shows_id))

def delete(request,id):
    x=Shows.objects.get(id=id)
    x.delete()
    return redirect('/')
def show_all(request):
    context={
        'myshows':Shows.objects.all(),
    }
    return render(request,'shows.html',context)
def this_show_details(request,id):
    context={
        'myshows':Shows.objects.get(id=id),
    }
    return render(request,'details.html',context)
def show_from_form(request):
    context={
        ''
    }
    return render(request,'details.html',context)

def show_edit(request,id):

    context={
        'myshows':Shows.objects.get(id=id),
    }
    return render(request,'edit.html',context)


def update_show(request,id):
    updated_show=Shows.objects.get(id=id)
    updated_show.title=request.POST['edit_form_title']
    updated_show.network=request.POST['edit_form_network']
    updated_show.release_date=request.POST['edit_form_res_date']
    updated_show.description=request.POST['edit_form_desc']
    updated_show.save()
    pass
    
def this_update_details(request,id):
    errors = Shows.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        context={
            'myshows':Shows.objects.get(id=id),
        }
        return render(request,'details.html',context)
def update_details(request):

    x=Shows.objects.update(title=request.POST['edit_form_title'],network=request.POST['edit_form_network'],release_date=request.POST['edit_form_res_date'],description=request.POST['edit_form_desc'])
    x.save()
    context={
        'myshows':Shows.objects.get(id=id),
    }
    return render(request,'details.html',context)