from django import forms
from .models import blog_post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = blog_post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'tinymce'}),
        }