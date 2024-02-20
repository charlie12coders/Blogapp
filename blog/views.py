from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signin(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('upasswd')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return redirect('/')
    return render(request,'Blogs/login.html')
def register(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        email=request.POST.get('uemail')
        password=request.POST.get('upasswd')
        newUser=User.objects.create_user(username=username,email=email,password=password)
        newUser.save()
        return redirect('/')
    return render(request,'Blogs/signup.html')
def home(request):
    context={'posts':Posts.objects.all()}
    return render(request,'Blogs/home.html',context)

def newPost(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        newPost=models.Posts(title=title,content=content,author=request.user)
        newPost.save()
        return redirect('/home')
    return render(request,'Blogs/newPost.html')

def myPost(request):
    context={'posts':Posts.objects.filter(author=request.user)}
    return render(request,'Blogs/myPost.html',context)

def signout(request):
    logout(request)
    return redirect('/')