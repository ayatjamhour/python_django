from django.shortcuts import   render, HttpResponse, redirect
def index(request):
    if "count" not in request.session:
      request.session["count"] = 1
    else:    
        request.session["count"] += 1
    context ={
        'counter' : request.session['count']
    }
    
    return render(request,'counter.html' , context)

def reset(request):
   request.session.clear()
   return redirect("/")
                                
def add(request):
        request.session['count']+=1
        return redirect("/")  
def destroy(request):
    request.session.clear() #del request.session['count']
    return redirect("/")  
