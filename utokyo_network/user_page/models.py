# utokyo_network/user_page/models.py
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save, pre_save, post_delete

from django.dispatch import receiver
import uuid


class TopicTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


# Skills are added by teh user to indicate topics they are proficient in
class SkillTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # 添加唯一的related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # 添加唯一的related_name
        blank=True
    )

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    bio = models.TextField(null=True)
    vote_ratio = models.IntegerField(blank=True, null=True, default=0)
    followers_count = models.IntegerField(blank=True, null=True, default=0)
    skills = models.ManyToManyField(SkillTag, related_name='personal_skills', blank=True)
    interests = models.ManyToManyField(TopicTag, related_name='topic_interests', blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    email_verified = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    """
    profile = UserProfile.objects.first()
    profile.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """

    def __str__(self):
        return str(self.user.username)
