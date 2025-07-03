"""
URL configuration for oibp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from businessperson import views

urlpatterns = [
    path('get_subcat', views.get_subcat, name='get_subcat'),
    path('layout', views.layout, name='layout'),
    path('home', views.home, name='home'),
    path('layout2', views.layout2, name='layout2'),
    path('home2', views.home2, name='home2'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('registration_store', views.registration_store, name='registration_store'),
    path('contact', views.contact, name='contact'),
    path('contact_store', views.contact_store, name='contact_store'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('idea', views.idea, name='idea'),
    path('idea_details/<int:id>', views.idea_details, name='idea_details'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('payment_done', views.payment_done, name='payment_done'),
    path('order', views.order, name='order'),
    path('payment_process', views.payment_process, name='payment_process'),
    path('success', views.success, name='success'),
    path('cart', views.cart, name='cart'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('forgot_password_check', views.forgot_password_check, name='forgot_password_check'),
    path('change_password', views.change_password, name='change_password'),
    path('change_password_update', views.change_password_update, name='change_password_update'),
   
    
]
