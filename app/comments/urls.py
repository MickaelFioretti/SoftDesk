from django.urls import path
from .views import CommentListView, CommentCreateView, IssueCommentListView

urlpatterns = [
    path("comment/", CommentListView.as_view(), name="Get all comments"),
    path("comment/create/", CommentCreateView.as_view(), name="Create a comment"),
    path(
        "issue_comment/<int:issue_id>",
        IssueCommentListView.as_view(),
        name="Get all comments for an issue",
    ),
]
