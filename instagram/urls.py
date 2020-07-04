from django.urls import path 
from . import views

urlpatterns = [
    path('',views.instagram_home,name='instagramhome'),
]