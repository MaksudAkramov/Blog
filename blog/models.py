from django.db import models

from account.models import Account
from django.db.models.deletion import CASCADE



class Category(models.Model):

    name = models.CharField(max_length=30, primary_key=True)
    about = models.TextField()
    photo = models.ImageField(upload_to = 'c_image', null = True)
    icon = models.ImageField(upload_to = 'с_icom', null = True)

    def str(self) -> str:
        return f"{self.name}"
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    author = models.ForeignKey(Account, on_delete=CASCADE, default=Account)
    approved_by = models.ManyToManyField(Account, related_name="+++", default=Account)
    created_time = models.DateTimeField(auto_now_add=True)

    
    

class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=CASCADE)
    created_time = models.DateField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    author = models.ForeignKey(Account, on_delete=CASCADE)
    liked_at = models.DateField(auto_now_add=True)  

    def save(self, *args, **kwargs) -> None:
        self.post.dislike_set.filter(author=self.author).delete()
        return super().save(*args, **kwargs)  

    

class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    author = models.ForeignKey(Account, on_delete=CASCADE)
    liked_at = models.DateField(auto_now_add=True)  

    def save(self, *args, **kwargs) -> None:
        self.post.like_set.filter(author=self.author).delete()
        return super().save(*args, **kwargs)


    