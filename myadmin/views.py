from django.shortcuts import render,redirect
from myadmin.models import Category,Subcategory
from innovators.models import Idea
from businessperson.models import Inquiry,Feedback,Profile,Order
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth import authenticate,login,logout


def layout(request):
    context = {}
    return render(request,'myadmin/layout.html',context)

def dashboard(request):
    id = request.user.id
    result=User.objects.get(pk=id)
    context = {'result':result}
    context = {}
    return render(request,'myadmin/dashboard.html',context)

#login

def login(request):
    context = {}
    return render(request,'myadmin/login.html',context)

def login_check(request):
    username=request.POST['username']
    password=request.POST['password']

    result=auth.authenticate(username=username,password=password)

    if result is None:
        messages.success(request,'Invalid Username or Password')
        return redirect('/myadmin/login')
    else:
        if result.is_superuser == 1:
            auth.login(request,result)
            return redirect('/myadmin/dashboard')
        else:
            messages.success(request,'Not An Admin')
            return redirect('/myadmin/login')

def logout(request):
    auth.logout(request)
    return redirect('/myadmin/login')

def common_form(request):
    context = {}
    return render(request,'myadmin/common_form.html',context)

def common_table(request):
    context = {}
    return render(request,'myadmin/common_table.html',context)

#category
def add_category(request):
    context = {}
    return render(request,'myadmin/add_category.html',context)

def category(request):
    result=Category.objects.all()
    context = {'result':result}
    return render(request,'myadmin/category.html',context)

def category_store(request):
    mycategoryname=request.POST['categoryname']
    # myfile=request.FILES['f']
    # #folder save
    # mylocation=os.path.join(settings.MEDIA_ROOT, 'upload')
    # obj=FileSystemStorage(location=mylocation)
    # obj.save(myfile.name,myfile)
    
    Category.objects.create(categoryname=mycategoryname)
    return redirect('/myadmin/add_category')

def category_delete(request,id):
    result=Category.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/category')

def category_edit(request,id):
    result=Category.objects.get(pk=id)
    context={'result':result}
    return render(request,'myadmin/category_edit.html',context)

def category_update(request,id):
    mycategoryname=request.POST['categoryname']
    # myfile=request.FILES['f']
    # #folder save
    # mylocation=os.path.join(settings.MEDIA_ROOT, 'upload')
    # obj=FileSystemStorage(location=mylocation)
    # obj.save(myfile.name,myfile)
    
    data={
          'categoryname':mycategoryname,
          # 'file_name':myfile.name
    }
    
    Category.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/category')

#subcategory

def add_subcategory(request):
    result=Category.objects.all()
    context = {'result':result}
    return render(request,'myadmin/add_subcategory.html',context)

def subcategory(request):
    result=Subcategory.objects.all()
    context = {'result':result}
    return render(request,'myadmin/subcategory.html',context)

def subcategory_store(request):
    mysubcategoryname=request.POST['subcategoryname']
    mycategory=request.POST['category']
    myfile=request.FILES['f']
    #folder save
    mylocation=os.path.join(settings.MEDIA_ROOT, 'upload')
    obj=FileSystemStorage(location=mylocation)
    obj.save(myfile.name,myfile)

    Subcategory.objects.create(subcategoryname=mysubcategoryname,category_id=mycategory,file_name=myfile.name)
    return redirect('/myadmin/add_subcategory')

def subcategory_delete(request,id):
    result=Subcategory.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/subcategory')

def subcategory_edit(request,id):
    categories    = Category.objects.all()
    result=Subcategory.objects.get(pk=id)
    context={'result':result,'categories':categories}
    return render(request,'myadmin/subcategory_edit.html',context)

def subcategory_update(request,id):
    mysubcategoryname=request.POST['subcategoryname']
    mycategoryid=request.POST['category']
    myfile=request.FILES['f']
    #folder save
    mylocation=os.path.join(settings.MEDIA_ROOT, 'upload')
    obj=FileSystemStorage(location=mylocation)
    obj.save(myfile.name,myfile)
    
    data={
          'subcategoryname':mysubcategoryname,
          'category_id':mycategoryid,
          'file_name':myfile.name
    }
    Subcategory.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/subcategory')


#users

def users(request):
    profiles=Profile.objects.filter(role='businessperson')
    context = {'profiles':profiles}
    return render(request,'myadmin/users.html',context)

def users_table(request,id):
    profiles=Profile.objects.get(pk=id)
    context = {'profiles':profiles}
    return render(request,'myadmin/users_table.html',context)

#innovators

def innovators(request):
    profiles1=Profile.objects.filter(role='innovator')
    context = {'profiles1':profiles1}
    return render(request,'myadmin/innovators.html',context)

def innovators_table(request,id):
    profiles1=Profile.objects.get(pk=id)
    context = {'profiles1':profiles1}
    return render(request,'myadmin/innovators_table.html',context)

#idea

def idea(request):
    result=Idea.objects.all()
    context = {'result':result}
    return render(request,'myadmin/idea.html',context)

def idea_table(request,id):
    result=Idea.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/idea_table.html',context)

#order

def order(request):
    context = {}
    return render(request,'myadmin/order.html',context)

#inquiry

def inquiry(request):
    result=Inquiry.objects.all()
    context = {'result':result}
    return render(request,'myadmin/inquiry.html',context)

#feedback

def feedback(request):
    user_id=request.user.id
    result=Feedback.objects.all()
    context = {'result':result,'user_id':user_id}
    return render(request,'myadmin/feedback.html',context)

#order

def order(request):
    orders=Order.objects.all()
    context={'orders':orders}
    return render(request,'myadmin/order.html',context)







