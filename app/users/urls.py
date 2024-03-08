"""
Users urls
"""

from django.urls import path
from users.views import CreateUserView

app_name = 'users'

urlpatterns = [
    path('add/', CreateUserView.as_view(), name='add'),
]