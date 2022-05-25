from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('pollsapp/', include('pollsapp.urls')),
    path('admin/', admin.site.urls),
]
