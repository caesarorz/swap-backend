"""
Users urls
"""

from django.urls import path
from users.views import CreateUserView, AuthTokenView

app_name = 'users'

urlpatterns = [
    path('add/', CreateUserView.as_view(), name='add'),
    path('authenticate/', AuthTokenView.as_view(), name='auth'),
]