from django.shortcuts import render
from django.http  import HttpResponse
from .forms import ImageUploadForm

# Create your views here.
def home(request):
   return render(request, 'insta/home.html')

def new_image(request):
   current_user = request.user
   if request.method == 'POST':
      form = ImageUploadForm(request.POST, request.FILES)
      if form.is_valid():
         image = form.save(commit=False)
         image_profile_id = current_user.id
         image.save()
      return redirect('home')

   else:
      form = ImageUploadForm()
   return render(request, 'new_image.html', {"form": form})