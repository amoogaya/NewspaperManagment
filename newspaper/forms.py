from django.forms import ModelForm
from .models import Articles, MyUser
from django.contrib.auth.forms import UserCreationForm


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'author', 'Category', 'body']


class UserForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'register_as']
