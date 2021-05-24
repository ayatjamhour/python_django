from django.db import models

# Create your models here.

class dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc =  models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

#

    # def basic_validator(self,post_data):
           #print(post_data)
    #       errors={}
    #   if len(post_data["first_name"] <1 :
    #       errors["first_name"]="please enter your name!"
    #   if len(post_data["last_name"] <1 :
    #           errors["last_name"]="please enter your name!"
    #   if len(post_data["dojo"] <1 :
    #       errors["dojo"]="please enter your name!"
    # return errors

class ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(dojo, related_name = "ninjas" , on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

def all_dojo():
     return dojo.objects.all()
# def all_ninja():
#      return ninja.objects.all()


  