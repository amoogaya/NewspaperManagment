from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, format_html


# Create your models here.
class MyUser(AbstractUser):
    roles = (
             ('User', 'User'),
             ('Author', 'Author')
    )

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField()
    register_as = models.CharField(max_length=200, choices=roles)
    REQUIRED_FIELDS = ['register_as']


class OurUser(MyUser):
    class Meta:
        verbose_name = 'our_user'


class Author(MyUser):
    position = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'authors'

    def __str__(self):
        return self.first_name + self.last_name


class Article(models.Model):
    category_choices = (
        ('sport', 'sport'),
        ('history', 'historical'),
        ('tourism', 'tourism'),
      )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=10, choices=category_choices)
    body = models.TextField(default='')
    is_published = models.BooleanField(default=False)

    class Meta:
        permissions = (("mark_published", "set article as published"),)

    def __str__(self):
        return self.title


class ArticleImages(models.Model):

    image = models.ImageField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def get_image_element(self):
        return format_html('<img src="%s" />' % escape(self.image.url))

    get_image_element.short_description = 'Image'
    get_image_element.allow_tags = True
