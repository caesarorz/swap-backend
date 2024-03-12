"""
Users urls
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import (CreateUserView, UserView, UserList, UserDetail,
                         CreateClientView, ClentView, ClientList, ClientDetail)


app_name = 'users'

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add/', CreateUserView.as_view(), name='add'),
    path('<int:pk>/', UserDetail.as_view(), name='detail'),
    path('', UserList.as_view(), name='list'),
    path('client/add/', CreateClientView.as_view(), name='add-client'),
    path('client/<int:pk>/', ClientDetail.as_view(), name='detail'),
    path('client/', ClientList.as_view(), name='list'),
]