from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required
from .models import Image

# Create your views here.
def home(request):
   images = Image.get_all()   
   
   return render(request, 'insta/home.html', {'images':images})

@login_required(login_url='/accounts/login/')
def new_image(request):
   current_user = request.user
   if request.method == 'POST':
      form = ImageUploadForm(request.POST, request.FILES)
      if form.is_valid():
         image = form.save(commit=False)
         
         image.save()
      return redirect('instagram-home')

   else:
      form = ImageUploadForm()
   return render(request, 'new_image.html', {"form": form})