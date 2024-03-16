"""
General URLs
"""

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/v1/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path('api/v1/user/', include('users.urls')),
    path('api/v1/', include('offers.urls')),
    path('api/v1/', include('payments.urls')),
]
