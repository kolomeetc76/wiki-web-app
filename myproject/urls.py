from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('summernote/', include('django_summernote.urls')),
]

