from django.contrib import admin
from django.urls import path, include
from cafe import views

urlpatterns = [
    path("", views.get_reviews, name="get-review-list"),
]
