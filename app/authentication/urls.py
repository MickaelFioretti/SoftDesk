from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    UserListView,
    UserDetailView,
    UserDetailAPIView,
)

urlpatterns = [
    path("connection/", TokenObtainPairView.as_view(), name="Login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="Token refresh"),
    path("register/", RegisterView.as_view(), name="Register a new user"),
    path("user/", UserListView.as_view(), name="user-list"),  # A voir si on garde
    path(
        "user/<int:pk>/", UserDetailView.as_view(), name="Get user details"
    ),  # A voir si on garde
    path(
        "user/me/",
        UserDetailAPIView.as_view(),
        name="All actions for the current user",
    ),
]
