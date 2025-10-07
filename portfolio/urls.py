from django.contrib import admin
from django.urls import path
from base import views as base_views

urlpatterns = [
    path('', base_views.home, name='home'),  # Homepage with contact form
    path('admin/', admin.site.urls),
]
