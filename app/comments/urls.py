from django.urls import path
from .views import CommentListView, CommentCreateView

urlpatterns = [
    path("comments/", CommentListView.as_view(), name="Get all comments"),
    path("comment/create/", CommentCreateView.as_view(), name="Create a comment"),
]
