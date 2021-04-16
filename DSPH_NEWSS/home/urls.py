from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.Top, name='home'),
    path('about', views.htnews, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('Vadodara', views.Vadodara, name='Vadodara'),
    path('Gujarat', views.Gujarat, name='Gujarat'),
    path('World', views.World, name='World'),
    path('IPL', views.IPL, name='IPL'),
    path('Business', views.Business, name='Business'),
    path('Entertaiment', views.Entertaiment, name='Entertaiment'),
    path('Covid', views.Covid, name='Covid'),
    path('Sports', views.Sports, name='Sports'),
    ##############copy of old project
  
    

]