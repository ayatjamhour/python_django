from django.db.models.fields import EmailField
from django.shortcuts import redirect, render,HttpResponse
from .models import User
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render (request,"index.html")
def add_new_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        userNew=User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],birthday=request.POST['birthday'],password=pw_hash)
        request.session['first_name']=request.POST['first_name']
        request.session['last_name']=request.POST['last_name']
        request.session['user_id']=userNew.id
        request.session['event']="Registered "
        return redirect ('/success')
def success(request):
    return render(request,'user.html')
def login_user(request):
    user_email=User.objects.filter(email=request.POST['login_email'])
    user_pass=request.POST['login_password']
    if len(user_email)!=0 :
        if user_email:
            logged_user=user_email[0]
            if bcrypt.checkpw(user_pass.encode(), logged_user.password.encode()):
                user_m=User.objects.get(email=request.POST['login_email'])
                request.session['first_name']=user_m.first_name
                request.session['last_name']=user_m.last_name
                request.session['user_id']=user_m.id
                request.session['event']="Logged In"
                return redirect('/success')
            else:return HttpResponse('The password you provided is Invalid')
    else:
        return HttpResponse('The email you provided is Invalid')
def log_out(request):
    request.session.flush()
    return redirect('/')