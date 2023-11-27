from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import comment_list

urlpatterns = [
    path("comment/",comment_list, name="comment"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)