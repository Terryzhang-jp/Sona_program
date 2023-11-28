from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)

   full_name = models.CharField(max_length=100)
   bio = models.TextField(max_length=100)
   image = models.ImageField(default='default.jpg', upload_to='user_images') 
   verified = models.BooleanField(default=False)

   def __str__(self):
       return self.full_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)
       instance.profile.save()

def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)