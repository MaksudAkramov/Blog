from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView, ListView, DetailView

from blog.forms import CommentForm, PostForm

from .models import Category, Comment, Like, Post

from blog.mixins import LoginPermissionMixin

class PostListView(LoginPermissionMixin, ListView):
    model = Post
    paginate_by = 10 
    
    
    

    def get_queryset(self):
        
        return Post.objects.all().order_by('-created_time')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['category_list'] = Category.objects.all()
        return context

class PostDetailView(LoginPermissionMixin, DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comment_form'] = CommentForm()
        context['comment_list'] = Comment.objects.filter(post=self.object).order_by('created_time')
        
        return context        

class CategoryListView(ListView,):
    model = Post
    template_name = 'blog/category_list.html'
    paginate_by = 6

    def get_queryset(self):
       return Post.objects.filter(category=self.request.resolver_match.kwargs['pk']).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['category_list'] = Category.objects.all()
        context.update({
            'category_list': Category.objects.all(),
        })
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
        return redirect('home') 
    context['form']= form
    return render(request, "blog/add_post.html", context)   

@login_required(login_url='login')
def like_post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if post:
                                    
        post.like_set.create(author=request.user)
        
        return redirect('post_detail', post_id)
        
    return render(request, '404.html')


@login_required(login_url='login')
def dislike_post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if post:
        post.dislike_set.create(author=request.user)
        
        return redirect('post_detail', post_id)
        
        
    return render(request, '404.html')     