from django import forms
from .models import Blog

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'photo', 'sound'] #여기에 어떤 필드를 받을 건지 적으면 됨 __all__하면 전체 받기 
