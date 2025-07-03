from django.shortcuts import render,redirect
from businessperson.models import *
from innovators.models import Idea
from myadmin.models import Category
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.core.mail import send_mail
from django.core import serializers
from django.http import HttpResponse



#layout

def layout(request):
    context = {}
    return render(request,'businessperson/layout.html',context)

#home

def home(request):
    id = request.user.id
    result=User.objects.get(pk=id)
    context = {'result':result}
    return render(request,'businessperson/home.html',context)

#layout2

def layout2(request):
    context = {}
    return render(request,'businessperson/layout2.html',context)

#home2

def home2(request):
    context = {}
    return render(request,'businessperson/home2.html',context)

#login

def login(request):
    context = {}
    return render(request,'businessperson/login.html',context)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(username=username,password=password)

    if result is None:
        messages.success(request, "invalid username or password")
        return redirect('/businessperson/login')    
    else:
        auth.login(request,result)
        return redirect('/businessperson/home')


#logout
def logout(request):
    auth.logout(request)
    return redirect('/businessperson/login')



#registration

def registration(request):
    context = {}
    return render(request,'businessperson/registration.html',context)

def registration_store(request):
    #Auth_user ________ model:User
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    username=request.POST['username']
    password=request.POST['password']
    cpassword=request.POST['cpassword']

    #Profile _______ model:Profile
    gender=request.POST['gender']
    contactno=request.POST['contactno']
    dob=request.POST['dob']
    address=request.POST['address']
    role=request.POST['role']

    if password == cpassword:
        user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        profile = Profile.objects.create(gender=gender,contact=contactno,dob=dob,address=address,user_id=user.id,role=role,password=password)
        messages.success(request,'registration Successfully')

        if profile.role == 'innovator':
            return redirect('/innovators/login')
        else:
            return redirect('/businessperson/login')
    else:
        messages.success(request,'password and confirm password mismatched')
        return redirect('/businessperson/registration')

    

#contact

def contact(request):
    context = {}
    return render(request,'businessperson/contact.html',context)

def contact_store(request):
    myname=request.POST['name']
    myemail=request.POST['email']
    mysubject=request.POST['subject']
    mymessage=request.POST['message']

    Inquiry.objects.create(name=myname,email=myemail,subject=mysubject,message=mymessage)
    return redirect('/businessperson/contact')

#aboutus

def aboutus(request):
    context = {}
    return render(request,'businessperson/aboutus.html',context)

#feedback

def feedback(request):
    context = {}
    return render(request,'businessperson/feedback.html',context)

def feedback_store(request):
    myrating=request.POST['rating']
    mycomment=request.POST['comment']
    user_id=request.user.id

    Feedback.objects.create(rating=myrating,comment=mycomment,user_id=user_id)
    return redirect('/businessperson/feedback')


#idea
def get_subcat(request):
    if request.method == 'POST':
        cat_id = request.POST['cat_id']
        subcategories = Subcategory.objects.filter(category_id=cat_id)
        subcategories_serialized = serializers.serialize('json', subcategories)
        # return JsonResponse(subcategories_serialized, safe=False)
        return HttpResponse(subcategories_serialized, content_type='application/json')
    else:
        return HttpResponse('Product Creation failed')
        
def idea(request):
    categories    = Category.objects.all()
    subcategories = Subcategory.objects.all()

    if request.method == "POST":
        mycategory = request.POST['category']
        mysubcategory = request.POST['subcategory']
        ideas2 = Idea.objects.filter(category_id=mycategory,subcategory_id=mysubcategory)
    else:
        ideas2 = Idea.objects.all()
    context = {'categories':categories,'subcategories':subcategories,'ideas2':ideas2}
    return render(request,'businessperson/idea.html',context)


#idea details

def idea_details(request,id):
    ideas2=Idea.objects.get(pk=id)
    context = {'ideas2':ideas2}
    return render(request,'businessperson/idea_details.html',context)

#add_to_cart

def add_to_cart(request,id):
    idea = Idea.objects.get(pk=id)
    # profile1=Profile.objects.get(pk=id)
    request.session['idea_id'] = idea.id
    request.session['idea_title'] = idea.title
    request.session['idea_price'] = idea.setupprice
    request.session['idea_duration'] = idea.setupduration
    request.session['idea_document'] = idea.file_name
    request.session['inn_id'] = idea.user.id
    request.session['inn_name'] = idea.user.first_name
    request.session['inn_email'] = idea.user.email
    # request.session['inn_contact'] = profile1.contact
    context = {}
    return redirect('/businessperson/cart')

#payment_done

def cart(request):
    context={}
    return render(request,'businessperson/add_to_cart.html',context)

def payment_done(request):
    context={}
    return render(request,'businessperson/payment_done.html',context)

#order
def order(request):
    idea_id = request.session['idea_id'] 
    innovator_id = request.session['inn_id']
    user_id = request.user.id
    profile = Profile.objects.get(user_id=user_id)
    Order.objects.create(idea_id=idea_id,innovator_id=innovator_id,profile_id=profile.id)
    return redirect('/businessperson/success')

def payment_process(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = int(request.session['idea_price'])*100

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"OIBP",
        "notes":{
            'name' : 'AK',
            'payment_for':'OIBP Test'
        }
    }

    id = request.user.id
    result = User.objects.get(pk=id)
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result}
    return render(request, 'businessperson/payment_process.html',context)

@csrf_exempt
def success(request):
    idea_id = request.session['idea_id'] 
    s=Idea.objects.get(pk=idea_id)
    context = {'s':s}
    return render(request,'businessperson/success.html',context)



def forgot_password(request):
    context = {}
    return render(request,'businessperson/forgot.html',context)

def forgot_password_check(request):
    myemail = request.POST['email']
    if User.objects.filter(email=myemail).exists():
        user = User.objects.get(email=myemail)
        profile = Profile.objects.get(user_id=user.id)
        subject = 'Online Innovators & Bussiness Portal'
        password = profile.password
        # message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
        message = f'Your Password is : {password}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [myemail, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/businessperson/login')


    else:
        messages.success(request,'Email Id is not found..')

def change_password(request):
    context = {}
    return render(request,'businessperson/change_password.html',context)

def change_password_update(request):
    username = request.user.username
    old_password  = request.POST['old_password']
    new_password  = request.POST['new_password']
    rnew_password = request.POST['rnew_password']

    if new_password == rnew_password:
        user = auth.authenticate(username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            profile = Profile.objects.get(user_id=request.user.id)
            Profile.objects.update_or_create(pk=profile.id,defaults={'password':new_password})
            messages.success(request, 'Password Updated Successfully')
            return redirect('/businessperson/login')
        else:
            messages.success(request, 'Invalid Password Try Again')
            return redirect('/businessperson/change_password/')     
    else:
         messages.success(request, 'Miss Match Password')
         return redirect('/businessperson/login')

