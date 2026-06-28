from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm_main.urls')),  # Barcha asosiy so‘rovlarni crm_main'ga yuboradi
]