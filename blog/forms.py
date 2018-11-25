from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

     class Meta:
         model = Post
         fields = ('author', 'title', 'text')

         widgets = {
             'title': forms.TextInput(attrs={'class': 'textinputclass'}), # textinputclass my own class
             'text': forms.Textarea(attrs={'class': 'aditable medium-aditor-textarea postcontent'}), # connect with css class, postcontent is my own class
         }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.TextInput(attrs={'class': 'aditable medium-aditor-textarea'}),
        }



