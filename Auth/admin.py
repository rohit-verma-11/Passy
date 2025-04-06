from django.contrib import admin
from .models import Credentials, Passwords

# Registering the models to make them accessible in the admin interface
# This allows you to manage the models through the Django admin panel.
# You can customize the admin interface further by creating custom ModelAdmin classes if needed.

admin.site.register(Credentials)
admin.site.register(Passwords)