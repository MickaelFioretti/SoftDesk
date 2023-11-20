from django.urls import path
from .views import IssueListView, IssueCreateView

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="Get all issues"),
    path("issue/create/", IssueCreateView.as_view(), name="Create an issue"),
]
