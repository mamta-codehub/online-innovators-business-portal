from django.shortcuts import render,redirect
from innovators.models import Idea
from myadmin.models import Category,Subcategory
from businessperson.models import *
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os




def layout(request):
    context = {}
    return render(request,'innovators/layout.html',context)

def dashboard(request):
    id = request.user.id
    result=User.objects.get(pk=id)
    context = {'result':result}
    context = {}
    return render(request,'innovators/dashboard.html',context)

def common_form(request):
    context = {}
    return render(request,'innovators/common_form.html',context)

def common_table(request):
    context = {}
    return render(request,'innovators/common_table.html',context)

#idea

def add_idea(request):
    result=Category.objects.all()
    subcategories=Subcategory.objects.all()
    context = {'result':result, 'subcategories':subcategories}
    return render(request,'innovators/add_idea.html',context)

def idea(request):
    id = request.user.id
    result=Idea.objects.filter(user_id=id)
    context = {'result':result}
    return render(request,'innovators/idea.html',context)

def idea_store(request):
    mycategory=request.POST['category']
    mysubcategory=request.POST['subcategory']
    mytitle=request.POST['title']
    mysmalldescription=request.POST['smalldescription']
    mylargedescription=request.POST['largedescription']
    mysetupprice=request.POST['setupprice']
    myfile=request.FILES['f']
    mylocation=os.path.join(settings.MEDIA_ROOT, 'upload')
    obj=FileSystemStorage(location=mylocation)
    obj.save(myfile.name,myfile)
    myfile1=request.FILES['f1']
    mylocation1=os.path.join(settings.MEDIA_ROOT, 'upload')
    obj=FileSystemStorage(location=mylocation1)
    obj.save(myfile1.name,myfile1)
    mysetupduration=request.POST['setupduration']
    id = request.user.id
    

    Idea.objects.create(category_id=mycategory,subcategory_id=mysubcategory,title=mytitle,smalldescription=mysmalldescription,largedescription=mylargedescription,setupprice=mysetupprice,setupduration=mysetupduration,file_name=myfile.name,file_name1=myfile1.name,user_id=id)
    return redirect('/innovators/add_idea')

def idea_update(request,id):
    mycategory         = request.POST['category']
    mysubcategory      = request.POST['subcategory']
    mytitle            = request.POST['title']
    mysmalldescription = request.POST['smalldescription']
    mylargedescription = request.POST['largedescription']
    mysetupprice       = request.POST['setupprice']
    mysetupduration    = request.POST['setupduration']

    if len(request.FILES) == 0:
        idea = Idea.objects.get(pk=id)
        file_name = idea.file_name
    else:
        # File Upload
        myfile             = request.FILES['f']
        mylocation         = os.path.join(settings.MEDIA_ROOT, 'upload')
        obj = FileSystemStorage(location=mylocation)
        obj.save(myfile.name,myfile)
        file_name = myfile.name

    if len(request.FILES) == 0:
        idea = Idea.objects.get(pk=id)
        file_name1 = idea.file_name1
    else:
        # File Upload
        myfile1             = request.FILES['f1']
        mylocation1         = os.path.join(settings.MEDIA_ROOT, 'upload')
        obj1 = FileSystemStorage(location=mylocation1)
        obj1.save(myfile1.name,myfile)
        file_name1 = myfile1.name
    

    data = {
        'category_id':mycategory,
        'subcategory_id':mysubcategory,
        'title':mytitle,
        'smalldescription':mysmalldescription,
        'largedescription':mylargedescription,
        'setupprice':mysetupprice,
        'setupduration':mysetupduration,
        'file_name':file_name,
        'file_name1':file_name1

    }   
    
    Idea.objects.update_or_create(pk=id,defaults=data)
    return redirect('/innovators/idea')


def idea_delete(request,id):
    result=Idea.objects.get(pk=id)
    result.delete()
    return redirect('/innovators/idea')

def idea_edit(request,id):
    categories    = Category.objects.all()
    subcategories = Subcategory.objects.all()
    result=Idea.objects.get(pk=id)
    context = {'result':result,'categories':categories,'subcategories':subcategories}
    return render(request,'innovators/idea_edit.html',context)



def idea_table(request,id):
    result=Idea.objects.get(pk=id)
    context = {'result':result}
    return render(request,'innovators/idea_table.html',context)

#order

def order(request):
    id = request.user.id
    orders=Order.objects.filter(innovator_id=id)
    context={'orders':orders}
    return render(request,'innovators/order.html',context)

#login

def login(request):
    context = {}
    return render(request,'innovators/login.html',context)

def login_check(request):
    username=request.POST['username']
    password=request.POST['password']

    result=auth.authenticate(username=username,password=password)

    if result is None:
        messages.success(request,'Invalid Username or Password')
        return redirect('/innovators/login')
    else:
        if Profile.objects.filter(user_id=result.id,role='innovator').exists():
            auth.login(request,result)
            return redirect('/innovators/dashboard')
        else:
            messages.success(request,'Invalid Username or Password')
            return redirect('/innovators/login')


def logout(request):
    auth.logout(request)
    return redirect('/innovators/login')

