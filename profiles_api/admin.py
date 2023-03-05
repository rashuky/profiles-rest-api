from django.contrib import admin
from profiles_api import models

# enable django admin for user profile module
admin.site.register(models.UserProfile)
