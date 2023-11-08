"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import RegisterView, UserListView, UserDetailView
from project.views import (
    ProjectListView,
    ProjectCreateView,
    ProjectAddContributorView,
    ContributorListView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/connection/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/users/", UserListView.as_view(), name="user-list"),
    path("api/user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("api/projects/", ProjectListView.as_view(), name="project-list"),
    path("api/project/create/", ProjectCreateView.as_view(), name="project-create"),
    path(
        "api/project/add_contributor/",
        ProjectAddContributorView.as_view(),
        name="project-add-contributor",
    ),
    path("api/contributors/", ContributorListView.as_view(), name="contributor-list"),
]
