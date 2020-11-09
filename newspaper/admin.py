from django.contrib import admin
from .models import OurUser, Authors, MyUser, Articles


class AuthorsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('None', {
            'fields': ('first_name', 'last_name', 'username')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_staff', 'is_active'),
        }),
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'Category', 'is_published')
    date_hierarchy = 'published_date'

    def has_change_permission(self, request, obj=None):
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
admin.site.register(Authors)
admin.site.register(OurUser)
admin.site.register(Articles, ArticleAdmin)
