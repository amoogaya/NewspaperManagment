from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns = [
    path('search/', views.search, name='search'),
]
