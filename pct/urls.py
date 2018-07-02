import markdownx.urls
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("instagram-hook/", views.instagram_hook),
    path("markdownx/", include(markdownx.urls)),
    path("<slug>/", views.detail, name="post-detail"),
]
