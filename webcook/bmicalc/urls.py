from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import BMI

urlpatterns = [
    path("bmi/",BMI, name="bmi"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)