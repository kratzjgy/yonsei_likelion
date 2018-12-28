from django import forms
from .models import Comment
from .models import Post

class SearchForm(forms.Form):
    word = forms.CharField(label='Search Word')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'message')
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'photo')
        
class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
