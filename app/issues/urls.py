from django.urls import path
from .views import (
    IssueListView,
    IssueCreateView,
    ProjectIssueListView,
    IssueUpdateView,
    IssueDeleteView,
)

urlpatterns = [
    path("issue/", IssueListView.as_view(), name="Get all issues"),
    path("issue/create/", IssueCreateView.as_view(), name="Create an issue"),
    path(
        "issue/update/<int:pk>",
        IssueUpdateView.as_view(),
        name="Update an issue",
    ),
    path(
        "issue/delete/<int:pk>",
        IssueDeleteView.as_view(),
        name="Delete an issue",
    ),
    path(
        "project_issue/<int:project_id>",
        ProjectIssueListView.as_view(),
        name="Get all issues for a project",
    ),
]
