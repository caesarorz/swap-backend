"""
Users urls
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import CreateUserView, ManageUserView

app_name = 'users'

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add/', CreateUserView.as_view(), name='add'),
    path('detail/', ManageUserView.as_view(), name='detail'),
]