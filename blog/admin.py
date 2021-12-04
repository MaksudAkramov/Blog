from django.contrib import admin

from account.models import Account
from blog.models import Category, Comment, Dislike, Like, Post

# Register your models here.

admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Dislike)