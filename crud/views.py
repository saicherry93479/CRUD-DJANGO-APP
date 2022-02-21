

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import crudModel
# Create your views here.

def index(request):
    data=crudModel.objects.all()
    if request.GET.get('search') is not None:
        if request.GET["search"] == 'ALL':
            data=crudModel.objects.all()
          
        if request.GET["search"] == 'COMPLETED':
            data=crudModel.objects.filter(completed=True)
           
        if request.GET["search"] == 'DELETED':
            data=crudModel.objects.filter(deleted=True)
            
        if request.GET["search"] == 'ACTIVE':
            data=crudModel.objects.filter(completed=False,deleted=False)
          
    
   
   
    # print("data is and type is  ",type(data[0].id))
    if request.method=="POST":
        name=request.POST.get("name")
        item=crudModel.objects.create(name=name)
        item.save()
        return render(request,"index.html",{"data":data})
    
    
    return render(request,'index.html',{'data':data})

def completed(request,pk):
    item=crudModel.objects.get(id=pk)
    item.completed=True
    item.save()
    return redirect('/')

def deleted(request,pk):
    item=crudModel.objects.get(id=pk)
    item.deleted=True
    item.save()
    return redirect('/')

def completeUndo(request,pk):
    item=crudModel.objects.get(id=pk)
    item.completed=False
    item.save()
    return redirect('/')
def deleteUndo(request,pk):
    item=crudModel.objects.get(id=pk)
    item.deleted=False
    item.save()
    return redirect('/')
