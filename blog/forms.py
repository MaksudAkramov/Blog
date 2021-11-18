from django import forms

from blog.models import Post

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 100}))   



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']   