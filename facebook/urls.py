from django.urls import path 
from . import views

urlpatterns = [
    path('',views.facebook_home,name='facebookhome'),
]