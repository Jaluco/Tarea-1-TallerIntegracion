from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('querys/', include('querys.urls')),
    path('admin/', admin.site.urls),
]
