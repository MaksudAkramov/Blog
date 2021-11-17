from django.contrib import admin

from account.models import Account
from blog.models import Comment, Post

# Register your models here.

admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Comment)