from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
   class Meta:
      model = Image
      exclude = ['image_profile', 'image_likes', 'image_comments']