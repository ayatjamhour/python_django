from django.db import models

# Create your models here.

class dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc =  models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(dojo, related_name = "ninjas" , on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

  