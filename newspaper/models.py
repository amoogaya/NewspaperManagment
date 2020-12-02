from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, format_html
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField
from django.utils import translation
from django.utils.translation import to_locale, get_language


# Create your models here.
class MyUser(AbstractUser):
    roles = (
             ('User', 'User'),
             ('Author', 'Author')
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

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.first_name + self.last_name


class Article(models.Model):
    category_choices = (
        ('sport', _('sport')),
        ('history', _('history')),
        ('tourism', _('tourism')),
      )

    author_en = models.ForeignKey(Author, on_delete=models.CASCADE)
    author_ar = models.ForeignKey(Author, on_delete=models.CASCADE)

    title_en = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)

    published_date_en = models.DateTimeField(auto_now=True)
    published_date_ar = models.DateTimeField(auto_now=True)

    category_en = models.CharField(max_length=10, choices=category_choices)
    category_ar = models.CharField(max_length=10, choices=category_choices)

    body_en = models.TextField(default='')
    body_ar = models.TextField(default='')

    is_published_en = models.BooleanField(default=False)
    is_published_ar = models.BooleanField(default=False)

    description_en = models.CharField(max_length=200, null=True)
    description_ar = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        permissions = (("mark_published", "set article as published"),)
        fields = ('get_author', )

    def __str__(self):
        return self.title

    @property
    def get_author(self):
        language = translation.get_language()
        if language == 'ar':
            return self.author_ar
        else:
            return self.author_en

    @property
    def get_title(self):
        language = translation.get_language()
        if language == 'ar':
            return self.title_ar
        else:
            return self.title_en

    @property
    def get_published_date(self):
        language = translation.get_language()
        if language == 'ar':
            return self.published_date_ar
        else:
            return self.published_date_en

    @property
    def get_category(self):
        language = translation.get_language()
        if language == 'ar':
            return self.category_ar
        else:
            return self.category_en

    @property
    def get_body(self):
        language = translation.get_language()
        if language == 'ar':
            return self.body_ar
        else:
            return self.body_en

    @property
    def get_is_published(self):
        language = translation.get_language()
        if language == 'ar':
            return self.is_published_ar
        else:
            return self.is_published_en

    @property
    def get_description(self):
        language = translation.get_language()
        if language == 'ar':
            return self.description_ar
        else:
            return self.description_en


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
