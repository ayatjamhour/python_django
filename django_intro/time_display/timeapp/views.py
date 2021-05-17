from django.shortcuts import render
from time import strftime, localtime

def index(request):
    context={
        'date': strftime('%b %d , %Y'),
        'time': strftime('%I:%M %p', localtime()),
        
    }

    return render(request,'time.html', context)