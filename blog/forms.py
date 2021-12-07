from django import forms
from django.db import models
from django.db.models.deletion import CASCADE
from account.models import Account

from blog.models import Post

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 100}))   



class PostForm(forms.ModelForm):
    author = models.ForeignKey(Account, on_delete=CASCADE)
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category']   