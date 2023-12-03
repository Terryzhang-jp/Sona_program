from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserMessage , Thread


admin.site.register(UserMessage)
admin.site.register(Thread)