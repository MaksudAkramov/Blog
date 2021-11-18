from django.contrib import admin
from django.urls import path


from blog.views import AboutUsView, PostDetailView, PostListView, add_post, comment_post

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', add_post, name='create'),
    path('<int:post_id>/comment', comment_post, name='comment'),
    path('aboutus', AboutUsView.as_view(), name='aboutus'),
]