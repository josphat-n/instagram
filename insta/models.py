from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   name = models.ForeignKey(User,on_delete=models.CASCADE)
   profile_photo = ImageField(blank=True, manual_crop="") 
   bio = models.TextField()
   
class Image(models.Model):
   image_name = models.CharField(max_length =30)
   image_image = ImageField(blank=True, manual_crop="")
   image_caption = models.TextField()
   image_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
   image_likes = models.IntegerField(default = 0)
   image_comments = models.TextField(blank = True)   
   
   def __str__(self):
      return self.image_name