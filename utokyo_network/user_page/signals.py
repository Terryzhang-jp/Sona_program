# utokyo_network/user_page/signals.py
from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from .models import User, UserProfile

#from django.contrib.auth import get_user_model

#User = get_user_model()


def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            name=instance.username,
            username=instance.username,
            #email=instance.email,
        )
        print('Profile Created!')

def update_profile(sender, instance, created, **kwargs):
    if not created:
        user_profile, _ = UserProfile.objects.get_or_create(user=instance)
        user_profile.username = instance.username
        #user_profile.email = instance.email
        user_profile.save()
        print('Profile updated!')

post_save.connect(create_profile, sender=User)
post_save.connect(update_profile, sender=User)