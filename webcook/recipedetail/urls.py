from django.contrib import admin
from django.urls import path
from .views import Details

urlpatterns = [
    path("recipe/",Details.as_view(), name="recipe"),
]