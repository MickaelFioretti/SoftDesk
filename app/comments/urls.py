from django.urls import path
from .views import (
    CommentListView,
    CommentCreateView,
    IssueCommentListView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path("comment/", CommentListView.as_view(), name="Get all comments"),
    path("comment/create/", CommentCreateView.as_view(), name="Create a comment"),
    path(
        "comment/update/<int:pk>",
        CommentUpdateView.as_view(),
        name="Update a comment",
    ),
    path(
        "comment/delete/<int:pk>",
        CommentDeleteView.as_view(),
        name="Delete a comment",
    ),
    path(
        "issue_comment/<int:issue_id>",
        IssueCommentListView.as_view(),
        name="Get all comments for an issue",
    ),
]
