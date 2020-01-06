from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
   path('', views.home, name ='instagram-home'),
   path('new_image', views.new_image, name='new-image'),
] 
