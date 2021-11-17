from django.db import models

from account.models import Account
from django.db.models.deletion import CASCADE



class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    text = models.TextField()
    author = models.ForeignKey(Account, on_delete=CASCADE, default=Account)
    approved_by = models.ManyToManyField(Account, related_name="+++", default=Account)
    created_time = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=CASCADE)
    created_time = models.DateField(auto_now_add=True)