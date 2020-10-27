from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', include('simple_app.urls'))
    path('admin/', admin.site.urls),
]
