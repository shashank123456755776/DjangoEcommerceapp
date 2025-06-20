from django.urls import path
from authcart import views

urlpatterns = [
path('signup/',views.signup,name='signup'),
path('login/',views.handlelogin,name='handlelogin'),
path('logout/',views.handlelogout,name='handlelogut'),
path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    # Add other URL patterns here
]
