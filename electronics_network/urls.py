from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('electronics.urls')),  # Подключаем API эндпоинты
    path('api-auth/', include('rest_framework.urls')),  # Эндпоинты для авторизации в DRF
]
