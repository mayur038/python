from django.shortcuts import render
from django.http import HttpResponse 

def hello(request):
    render(request,'hello.html',{'name':'admin'})
# Create your views here.
