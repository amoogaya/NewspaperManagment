from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, format_html
from django.utils.translation import gettext_lazy as _
from django.utils import translation


# Create your models here.
class MyUser(AbstractUser):
    roles = (
             ('User', _('User')),
             ('Author', _('Author')),
    )

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(_('first name'), max_length=200, blank=True)
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
        verbose_name = _('our user')
        verbose_name_plural = _('our users')


class Author(MyUser):
    position = models.CharField(max_length=200, blank=True)
    position_en = models.CharField(max_length=200, blank=True)
    position_ar = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.first_name + self.last_name

    @property
    def get_position(self):
        if translation.get_language() == 'ar':
            self.position = self.position_ar
        else:
            self.position_en = self.position_en
        return self.position


class Article(models.Model):
    category_choices = (
        ('sport', _('sport')),
        ('history', _('history')),
        ('tourism', _('tourism')),
      )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=10, choices=category_choices)
    body = models.TextField(default='')
    is_published = models.BooleanField(default=False)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        permissions = (("mark_published", "set article as published"),)

    def __str__(self):
        return self.title


class ArticleImages(models.Model):
    image = models.ImageField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('articles image')
        verbose_name_plural = _('articles images')

    def get_image_element(self):
        return format_html('<img src="%s" />' % escape(self.image.url))

    get_image_element.short_description = 'Image'
    get_image_element.allow_tags = True


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    @property
    def get_title(self):
        if translation.get_language() == 'ar':
            return self.title_ar
        else:
            return self.title_en
