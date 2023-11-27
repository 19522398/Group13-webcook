from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomePage, SearchResult, NotFound, Member

urlpatterns = [
    path("",HomePage.as_view()),
    path("results/", SearchResult.as_view(), name="results"),
    path("member/",Member.as_view(),name="member"),
    path("notfound/",NotFound.as_view(),name="not_found")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)