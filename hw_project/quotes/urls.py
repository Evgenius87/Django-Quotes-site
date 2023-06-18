from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>/", views.main, name="root_paginate"),
    path('create_new_quote/', views.create_new_quote, name='create_new_quote'),
    path("author/<int:_id>", views.about_author, name="about_author"),
]
