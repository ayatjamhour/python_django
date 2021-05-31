from django.db import models
from django.db.models.deletion import CASCADE
from login_register.models import *

class messages(models.Model):
    post = models.TextField()
    owner = models.ForeignKey(users,related_name="posts",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class comment(models.Model):
    comm = models.TextField()
    postown=models.ForeignKey(messages,related_name='comments',on_delete=CASCADE)
    userown=models.ForeignKey(users,related_name='ownedby',on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def get_user_cars(id):
    user= users.objects.get(id=id)
    return user
def create_post(po,id):
    messages.objects.create(post=po,owner=id)
    return True
