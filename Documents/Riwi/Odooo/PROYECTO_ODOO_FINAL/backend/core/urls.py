from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí conectamos tus leads con el prefijo /api/
    path('api/', include('leads.urls')),
]