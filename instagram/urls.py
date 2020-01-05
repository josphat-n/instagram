from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('insta.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
   
]