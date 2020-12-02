from django.db import models
from django.contrib import admin
from .widgets import ImageCustomWidget
from djrichtextfield.models import RichTextWidget
from .models import OurUser, Author, MyUser, Article, ArticleImages
from translated_fields import TranslatedFieldAdmin
from django.utils.translation import gettext_lazy as _

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email')

    fieldsets = (
        ('None', {
            'fields': ('first_name', 'last_name', 'username', 'email')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_staff', 'is_active'),
        }),
    )


class ArticleImageAdmin(admin.StackedInline):
    model = ArticleImages
    extra = 3
    max_num = 5
    fields = ('image', )
    formfield_overrides = {
        models.ImageField: {'widget': ImageCustomWidget},
    }


class ImageAdmin(admin.ModelAdmin):
    model = ArticleImages
    list_display = ('get_image_element', )
    fields = ('image', 'article', )


class ArticleAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    list_display = ('title_ar', 'author_ar', 'category_ar', 'is_published_ar', 'body_ar', 'description_ar')
    fields = ('title_ar', 'author_ar', 'category_ar', 'body_ar')
    date_hierarchy = 'published_date'
    inlines = [ArticleImageAdmin]
    formfield_overrides = {
        models.TextField: {'widget': RichTextWidget},
    }

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if obj.author.username == request.user.username:
                return True
            else:
                return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.author.username == request.user.username:
                return True
            else:
                return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = Author.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Register your models here.
admin.site.register(MyUser)
admin.site.register(Author, AuthorAdmin)
admin.site.register(OurUser)
admin.site.register(Article, ArticleAdmin)
