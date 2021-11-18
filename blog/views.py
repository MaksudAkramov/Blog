from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView, ListView, DetailView

from blog.forms import CommentForm, PostForm

from .models import Comment, Post

from blog.mixins import LoginPermissionMixin

class PostListView(LoginPermissionMixin, ListView):
    model = Post
    paginate_by = 10 
    
    
    

    def get_queryset(self):
        
        return Post.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        return context

class PostDetailView(LoginPermissionMixin, DetailView):
    model = Post
    # query_set = Comment.objects.all()
        
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comment_form'] = CommentForm()
        context['comment_list'] = Comment.objects.filter(post=self.object)
        # context['comment_list'] = self.object.comment_set.all()
        return context        


class  AboutUsView(TemplateView):
    template_name = "about.html"    


@login_required(login_url='login')
def comment_post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if post:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            post.comment_set.create(author=request.user, text=form.cleaned_data['comment'])
            return redirect('post_detail', post_id)
    return render(request, '404.html')    


@login_required(login_url='login')
def add_post(request):
    posts = Post.objects.all()
    context ={}
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'blog/post_list.html', context={'posts': posts}) 
    context['form']= form
    return render(request, "blog/add_post.html", context)    