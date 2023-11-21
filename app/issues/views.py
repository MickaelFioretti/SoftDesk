from rest_framework import generics, status
from rest_framework.response import Response
from .models import Issue
from .serializers import IssueSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


# ---- Issue views ----
class IssueListView(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get(self, request):
        response_data = {}
        issue = Issue.objects.all()
        serializer = IssueSerializer(issue, many=True)
        response_data["response"] = "Successfully retrieved all issues."
        response_data["data"] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


class IssueCreateView(generics.CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def create(self, request):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            issue = serializer.save()
            response_data["response"] = "Successfully created a new issue."
            response_data["name"] = issue.name
        else:
            response_data = serializer.errors
        return Response(response_data, status=status.HTTP_201_CREATED)


class ProjectIssueListView(APIView):
    def get(self, request, project_id):
        issues = Issue.objects.filter(project_id=project_id).order_by("id")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(issues, request)
        serializer = IssueSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
