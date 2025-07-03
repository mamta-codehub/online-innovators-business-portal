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
from myadmin import views

urlpatterns = [
    
    path('layout', views.layout, name='layout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('common_form', views.common_form, name='common_form'),
    path('common_table', views.common_table, name='common_table'),
    path('add_category', views.add_category, name='add_category'),
    path('category', views.category, name='category'),
    path('category_store', views.category_store, name='category_store'),
    path('category_delete/<int:id>', views.category_delete, name='category_delete'),
    path('category_edit/<int:id>', views.category_edit, name='category_edit'),
    path('category_update/<int:id>', views.category_update, name='category_update'),
    path('add_subcategory', views.add_subcategory, name='add_subcategory'),
    path('subcategory', views.subcategory, name='subcategory'),
    path('subcategory_store', views.subcategory_store, name='subcategory_store'),
    path('subcategory_delete/<int:id>', views.subcategory_delete, name='subcategory_delete'),
    path('subcategory_edit/<int:id>', views.subcategory_edit, name='subcategory_edit'),
    path('subcategory_update/<int:id>', views.subcategory_update, name='subcategory_update'),
    path('users', views.users, name='users'),
    path('users_table/<int:id>', views.users_table, name='users_table'),
    path('innovators', views.innovators, name='innovators'),
    path('innovators_table/<int:id>', views.innovators_table, name='innovators_table'),
    path('idea', views.idea, name='idea'),
    path('idea_table/<int:id>', views.idea_table, name='idea_table'),
    path('order', views.order, name='order'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('feedback', views.feedback, name='feedback'),

]

