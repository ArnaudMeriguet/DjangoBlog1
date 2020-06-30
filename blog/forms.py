from django import forms
from .models import Post, Education,Work

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)

class edForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=('year1','year2','title','details',)

        
class workForm(edForm):
    class Meta:
        model=Work
        fields=('year1','year2','months','title','details',)