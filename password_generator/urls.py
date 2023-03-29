from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

path('',views.home,name='home'),
# path('',views.home_tempelate,name='home_tempelate'),
path('password/',views.password,name='password'),
path('about/',views.about,name='about'),
# path('error/', views.error, name='error'),
]