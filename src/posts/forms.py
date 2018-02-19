from django.forms import ModelForm
from django import forms
from posts.models import Post


class PostForm(ModelForm):

    class Meta:

        model = Post
        widgets = {'title': forms.TextInput(attrs={'size': 41}),
                   'summary': forms.TextInput(attrs={'size': 41}),
                   'url': forms.TextInput(attrs={'size': 41}),
                   'publish_date': forms.TextInput(attrs={'size': 41})}

        fields = '__all__'
        exclude = ['owner']