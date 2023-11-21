from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ContributorCreateView,
    ContributorListView,
)

urlpatterns = [
    path("projects/", ProjectListView.as_view(), name="Get all projec"),
    path("project/create/", ProjectCreateView.as_view(), name="Create a project"),
    path(
        "project/add_contributor/",
        ContributorCreateView.as_view(),
        name="Add contributor to a project",
    ),
    path("contributors/", ContributorListView.as_view(), name="Get all contributors"),
]