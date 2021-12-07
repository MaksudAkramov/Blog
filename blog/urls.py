from django.contrib import admin
from django.urls import path


from .views import AboutUsView, CategoryListView, PostDetailView, PostListView, add_post, comment_post, dislike_post, like_post
# dislike_post, like_post

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('', CategoryListView.as_view(), name='categories'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', add_post, name='create'),
    path('<post_id>/comment', comment_post, name='comment'),
    path('<post_id>/like', like_post, name='like'),
    path('<post_id>/dislike', dislike_post, name='dislike'),
    path('aboutus', AboutUsView.as_view(), name='aboutus'),
    # path('category/<slug:pk>', CategoryListView.as_view()
]