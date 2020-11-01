from django.contrib import admin
from .models import OurUser, Authors, MyUser
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Authors)
admin.site.register(OurUser)
