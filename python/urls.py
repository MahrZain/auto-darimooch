"""
URL configuration for python project.

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
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new


from django.conf import settings

from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('about/', views.about, name= 'about' ),
    path('login/', views.login_view, name= 'login' ),
    path('login-user/', views.loginUser, name= 'login-user' ),
    path('register/', views.register, name= 'register' ),
    path('logout/', views.logoutUser, name= 'logout' ),
    path('register-user/', views.registerUser, name= 'register-user' ),
    path('faq/', views.faq, name= 'faq' ),
    path('contact/', views.contact, name='contact' ),
    path('savcontact/', views.savcontact, name='savcontact' ),
    path('allproducts/', views.allpro, name='allproducts' ),
    path('search/', views.search, name='search' ),
    path('products/<int:new_slug>', views.viewproducts, name='products' ),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)