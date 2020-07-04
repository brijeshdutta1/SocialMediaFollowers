from django.shortcuts import render


def facebook_home(request): 
    return render(request,'facebook/facebook.html')