from django.urls import path 
from ecommerceapp import views
from django.urls import path

urlpatterns = [
   path('',views.index,name="index"),  
   path('contact',views.contact,name="contact"),
   path('about',views.about,name="about"),
   path('signin',views.signin,name="signin")
]