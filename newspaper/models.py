from django.db import models
from django.contrib.auth.models import AbstractUser

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


class Authors(MyUser):
    position = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'authors'

    def __str__(self):
        return self.first_name + self.last_name


class Articles(models.Model):
    category_choices = (
        ('sport', 'sport'),
        ('history', 'historical'),
        ('tourism', 'tourism'),
      )
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    Category = models.CharField(max_length=10, choices=category_choices)
    body = models.TextField(default='')
    is_published = models.BooleanField(default=False)

    class Meta:
        permissions = (("mark_published", "set article as published"),)

    def __str__(self):
        return self.title
