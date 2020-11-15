from django.contrib import admin
from .models import OurUser, Authors, MyUser, Articles, ArticleImages
from djrichtextfield.models import RichTextWidget
from django.db import models


class AuthorsAdmin(admin.ModelAdmin):
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


class ArticleImagesAdmin(admin.StackedInline):
    model = ArticleImages
    extra = 3
    max_num = 5


class ImagesAdmin(admin.ModelAdmin):
    model = ArticleImages
    list_display = ('get_image_element', )
    fields = ('images', 'articles', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'body')
    date_hierarchy = 'published_date'
    empty_value_display = 'empty'
    inlines = [ArticleImagesAdmin]
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
            kwargs["queryset"] = Authors.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Register your models here.
admin.site.register(MyUser)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(OurUser)
admin.site.register(Articles, ArticleAdmin)
admin.site.register(ArticleImages, ImagesAdmin)


