from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=999)#title of the post and its limit of how many letters they can type
    content = models.TextField()#how much we want the user to be able to type in the post (Which could be alot of words so its left blank so that it will be indefinite)
    date_posted = models.DateTimeField(default=timezone.now)# when a post is made, grab the current time
    author = models.ForeignKey(User, on_delete=models.CASCADE)# if a user gets deleted so will all of thier posts


def __str__(self):#magic method
    return self.title#























































































