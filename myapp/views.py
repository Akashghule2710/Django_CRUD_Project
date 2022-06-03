import email
from pkgutil import get_data
from re import U
from urllib import request
from urllib.request import Request
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"myapp/insert.html")

def InsertData(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    newuser=student.objects.create(firstname=fname,lastname=lname,email=email,contact=contact)

#after insert render on show.html
    return redirect('showtable')
#show table view
def ShowTable(request):
    all_data = student.objects.all()
    return render (request,"myapp/show.html",{'key1':all_data})

#edit page view
def EditPage(request,pk):
    get_data=student.objects.get(id=pk)
    return render(request,"myapp/edit.html",{'key2':get_data})

#update data view
def UpdateData(request,pk):
    udata=student.objects.get(id=pk)
    udata.firstname=request.POST['fname']
    udata.lastname=request.POST['lname']
    udata.email=request.POST['email']
    udata.contact=request.POST['contact']
    #query for update
    udata.save()

    return redirect('showtable')

#delete data view

def DeleteData(request,pk):
    ddata=student.objects.get(id=pk)
    #query for delete
    ddata.delete()

    return redirect("showtable")