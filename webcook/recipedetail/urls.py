from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import get_queryset

urlpatterns = [
    path("recipe/", get_queryset, name="recipe"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)