"""
URL configuration for studybud1 project.

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
from django.urls import path

from studybud1 import views
from django.conf import settings 
from django.urls.conf import include 
from django.conf.urls.static import static
from .views import image_request 
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/', views.aboutus),
    path('', views.HOME),
    path('course/', views.course),
    path('submitform/', views.submitform ,name='submitform'),
    path('userform/', views.userform),
    path('course/<int:courseId>', views.coursed),
    path('calculater/', views.calculater),
    path('images/',views.image_request ,name='sampleapp'),  
    path('newsDetail/<slug>', views.newsDetail),
    path('vedios/', include('vedios.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
  
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
