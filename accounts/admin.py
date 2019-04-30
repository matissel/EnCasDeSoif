from django.contrib import admin
from accounts.models import UserProfile

# Specify the user model name
admin.site.register(UserProfile)