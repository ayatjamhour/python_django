from django.db import models
from django.db.models.fields import DateTimeField

#manager
class ShowManager(models.Manager):
    def basic_validator(self,post_data):
        errors={}
        d= DateTimeField(auto_now_add=True)
        if len(post_data['form_title'])<2:
            errors['form_title']="your title should be at least 2 characters"
        if len(post_data['form_network'])<2:
            errors['form_network']="your network name should be at least 3 characters"
        if post_data['form_desc'] !="":
            if len(post_data['form_desc'])<10:
                errors['form_desc']="your description should be at least 10 characters"
        if post_data['form_res_date']<=str(d):
            errors['form_res_date']="your date should be in the past"
        return errors
    def edit_validator(self,post_data):
        errors={}
        d= DateTimeField(auto_now_add=True)
        if len(post_data['edit_form_title'])<2:
            errors['edit_form_title']="your title should be at least 2 characters"
        if len(post_data['edit_form_network'])<2:
            errors['edit_form_network']="your network name should be at least 3 characters"
        if post_data['edit_form_desc'] !="":
            if len(post_data['edit_form_desc'])<10:
                errors['edit_form_desc']="your description should be at least 10 characters"
        if post_data['edit_form_res_date']<=str(d):
            errors['edit_form_res_date']="your date should be in the past"
        return errors
        
#SHOWS
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    objects = ShowManager()
