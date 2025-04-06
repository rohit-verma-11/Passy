from django.db import models

# Create your models here.
class Credentials(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True, blank=True)

class Passwords(models.Model):
    user = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)