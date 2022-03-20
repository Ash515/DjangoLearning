from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

#creating a view request function 

def say_hello(request):
    return render(request,'hello.html',{'name':'Ashwin'})
