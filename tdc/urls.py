from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('simple_app.urls')),
    path('admin/', admin.site.urls),
]
