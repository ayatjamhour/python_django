from django.shortcuts import render
def index(request):
    return render(request,"index.html")
        
def user(request):
    
    name = request.POST['txt']
    location = request.POST['loc']
    language = request.POST['lang']
    comment = request.POST['tex']
    context = {
    	"name" : name,
    	"location" : location,
    	"language":language,
    	"comment":comment
    }
    return render(request,"result.html",context)