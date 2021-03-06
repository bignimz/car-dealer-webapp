from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100, blank=True, null=True)
    google_plus_link = models.URLField(max_length=100, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name

        

class Topbar(models.Model):
    topbar_phone = models.CharField(max_length=255)
    topbar_email = models.EmailField(max_length=255)
    open_hours = models.CharField(max_length=255)

    def __str__(self):
        return self.topbar_phone
