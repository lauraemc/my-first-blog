from django import forms

from .models import Post #imports post model

class PostForm(forms.ModelForm):#name of form = PostForm
    #tell Django which model should be used to create this form (model = Post)

    class Meta:
        model = Post
        fields = ('title', 'text',)