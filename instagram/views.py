from django.shortcuts import render
# Create your views here.

def instagram_home(request): 
    return render(request,'instagram/instagram.html')