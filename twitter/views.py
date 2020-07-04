from django.shortcuts import render

def twitter_home(request):
    return render(request,'twitter/twitter.html')