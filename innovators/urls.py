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
from innovators import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('common_form', views.common_form, name='common_form'),
    path('common_table', views.common_table, name='common_table'),
    path('add_idea', views.add_idea, name='add_idea'),
    path('idea', views.idea, name='idea'),
    path('idea_store', views.idea_store, name='idea_store'),
    path('idea_delete/<int:id>', views.idea_delete, name='idea_delete'),
    path('idea_edit/<int:id>', views.idea_edit, name='idea_edit'),
    path('idea_update/<int:id>', views.idea_update, name='idea_update'),
    path('idea_table/<int:id>', views.idea_table, name='idea_table'),
    path('order', views.order, name='order'),
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


