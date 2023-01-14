from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=250,null=True,blank=True)
    dob = models.DateField(default=date.today,verbose_name='D.O.B.',blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    profile_created = models.DateTimeField(default=timezone.now,verbose_name='Date Created')

    def __str__(self):
        return f"{self.user.username}'s Profile".capitalize()

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
