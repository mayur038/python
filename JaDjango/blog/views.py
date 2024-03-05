from collections import UserDict
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Features
from django.contrib.auth.models import User,auth
from django.contrib import messages


def say_hello(request):  
   
    return HttpResponse('<h1>Hey wealcome </h1>')

# Create your views here.
  
def index(request):
    ft= Features.objects.all()
    
    return render(request,'index.html',{'feature':ft})


def register(request):
    
    if request.method == 'POST':
        
        name = request.POST['name']
        emails = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['cpassword']

        if password == password2:
            
            if User.objects.filter(email=emails).exists():
                messages.info(request,'User already exists')
                return redirect('register')
                
            else:
                user = User.objects.create_user(username=name,email=emails,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password is not same as repeat password')
            return redirect('register')
    else:    
         return render(request,'register.html')

def login(request):

    if request.method == 'POST':
        emails = request.POST['email']
        password = request.POST['password']

        user  = auth.authenticate(username=emails,password=password)
      
        if user is not None:
            auth.login(request,user)
            messages.info(request,'success')
            return redirect('login')
        else:
            messages.info(request,'Invalid')
            return redirect('login')
    else:
        return render(request,'login.html',{})

def post(request,pk):
   return render(request,'post.html',{'pk':pk})