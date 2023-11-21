from django.urls import path
from .views import IssueListView, IssueCreateView, ProjectIssueListView

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="Get all issues"),
    path("issue/create/", IssueCreateView.as_view(), name="Create an issue"),
    path(
        "project/<int:project_id>/issues/",
        ProjectIssueListView.as_view(),
        name="Get all issues for a project",
    ),
]