from django.shortcuts import redirect, render
import random
def guess(request):
    usernum=-1
    if 'flag' in request.session and  request.session['flag']!=1: 
        print("the initial value for the flag:" ,request.session['flag'])
        if request.method == "GET": 
            request.session['random_num']=random.randint(1,100) 
            print("the random generated number is:",request.session['random_num'])
            request.session['played_times']=0   
    elif 'flag' not in request.session:
            request.session['flag']=0
            request.session['random_num']=random.randint(1,100) 
            print("the random generated number is:",request.session['random_num'])   
            request.session['played_times']=0    
    if 'user_num' in request.session:
        usernum=request.session['usernum'] 

        if request.session['usernum'] !=-1:
            print("user number is:",request.session['usernum']) 
            
            if(request.session['usernum'] == request.session['random_num']): 
                print("sucess")
                print(f"you took {request.session['played_times']} of attempts")
            elif(request.session['usernum'] > request.session['random_num']):
                print("Too High!")
                if request.session['played_times'] < 6: 
                    request.session['played_times']+=1 
                    print("played_times: ",request.session['played_times']) 
            elif(request.session['usernum'] < request.session['random_num']):
                print("Too Low!") 
                if request.session['played_times'] < 6: 
                    request.session['played_times']+=1 
                    print("played_times: ",request.session['played_times']) 
                    
    request.session['usernum']=-1 
    request.session['flag']=0 
    context = {
            "usernum":usernum 
        
    }
    return render(request, 'index.html', context)

def result(request):
    if request.method == "POST": 
        if request.POST['usernum'] !="": 
            request.session['usernum']= int(request.POST['usernum']) 
 
    request.session['flag']=1 
    return redirect('/')  

def reset(request):
    if 'usernum' in request.session:
        del request.session['usernum']

    if 'random_num' in request.session:    
        del request.session['random_num']  
   
  

    return redirect('/') 


def send_name(request):
    if request.method =='POST':
        request.session['name']=request.POST['username']

        return render(request, 'info.html')