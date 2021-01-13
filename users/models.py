from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from PIL import Image
from create_users.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  


    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image)
        if img.height > 300 or img.width > 300:
            img.thumbnail((200, 200))
            fh = storage.open(self.image.name, "wb")
            picture_format = 'png'
            img.save(fh, picture_format)
            fh.close()    
