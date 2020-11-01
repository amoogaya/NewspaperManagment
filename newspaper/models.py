from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyUser(User):
    roles = (
             ('User', 'User'),
             ('Author', 'Author')
    )
    resigt_as = models.CharField(max_length=200, choices=roles)
    REQUIRED_FIELDS = ['resigt_as']


class OurUser(MyUser):
    class Meta:
        db_table = 'OurUser'


class Authors(MyUser):
    position = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'Authors'

    def __str__(self):
        return self.first_name + self.last_name


class Articles(models.Model):
    Category_Choices = (
        ('sport', 'sport'),
        ('history', 'historical'),
        ('tourism', 'tourism'),
      )
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    Category = models.CharField(max_length=10, choices=Category_Choices)
    body = models.TextField(default='')

    def __str__(self):
        return self.title
