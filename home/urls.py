from django.contrib import admin
from django.urls import path, include
from .views import homeView

#for settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homeView, name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)