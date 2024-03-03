from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    ogrenciler=Ogrenciler.objects.all()
    context={
        "ogrenciler":ogrenciler
    }
    return render(request, 'index.html',context)

def detay(request,pk):
    ogrenci=Ogrenciler.objects.filter(id=pk)
    context={
        "ogrenci":ogrenci

    }

    return render(request,'detay.html',context)

def ogrenciCreate(request): 
    form=OgrenciForm()
    if request.method=="POST":
        form=OgrenciForm(request.POST,request.FILES)
        if form.is_valid:
            ogrenci=form.save(commit=False)
            ogrenci.owner=request.user
            ogrenci.save()
            return redirect("index")
        else:
            print(form.errors)
        
    context={
        "form":form
    }
    return render(request,'ogrenciCreate.html',context)

def filtre(request,id):
    ogrenciler=Ogrenciler.objects.filter(owner=id)
    context={
        "ogrenciler":ogrenciler
    }
    return render(request,'filter.html',context)
