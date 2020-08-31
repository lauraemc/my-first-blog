from django import forms

from .models import Post, WorkElement, EduElement, Skills, Extra #imports post model

class PostForm(forms.ModelForm):#name of form = PostForm
    #tell Django which model should be used to create this form (model = Post)

    class Meta:
        model = Post
        fields = ('title', 'text_preview','text','image_path')
    # is text_preview required?

class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkElement
        fields = ('dates', 'employer','location','position','assignments',)

class EduForm(forms.ModelForm):
    class Meta:
        model = EduElement
        fields = ('dates', 'title','subTitle','text',)
        
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('fluent', 'experience',)

class ExtraForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = ('text',)

