from django.forms import ModelForm, Widget
from .models import Article, MyUser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'category', 'body']


class UserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'register_as']


BIRTH_YEAR_CHOICES = ['1990', '1991']
FAVORITE_COLORS = [
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('green', 'Green'),
]


class CommentForm(forms.Form):
    comment = forms.CharField()
    image = forms.ImageField()
