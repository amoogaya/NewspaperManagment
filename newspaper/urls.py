from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name='newspaper'
urlpatterns = [

    path('',view=views.IndexView.as_view(),name='index'),
    path('<int:pk>/',view=views.DetailedView.as_view(),name='detailed'),
    path('add/',views.article_add,name='addArticle'),


]
