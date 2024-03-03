from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import login as lgn,logout as lgout,authenticate
# Create your views here.
def register(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid:
            form.save()
            # user=form.save(commit=False)
            # user.username=user.username.lower()
            # user.save()
            return redirect("login")
    context={
        "form":form
    }
    return render(request,"register.html",context)
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        userpass=request.POST["userpass"]
        user=authenticate(request,username=username,password=userpass)
        if user is not None:
            lgn(request,user)
            return redirect("index")
        else:
            return render(request,"login.html")
        # context={
        #     "username":username
        #     "userpass":userpass
        # }
    return render(request,"login.html")
def logout(request):
    lgout(request)
    return redirect("index")