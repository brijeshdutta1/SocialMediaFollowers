from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('pages.urls')),
    path('instagram/',include('instagram.urls')),
    path('facebook/',include('facebook.urls')),
    path('twitter/',include('twitter.urls')),
    path('admin/', admin.site.urls),

]
