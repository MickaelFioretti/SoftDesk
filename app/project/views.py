# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Project, Contributor
from .serializers import (
    ProjectSerializer,
    ContributorGetSerializer,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


# ---- Project views ----
class ProjectListView(APIView):
    def get(self, request):
        response_data = {}
        project = Project.objects.all().order_by("id")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(project, request)
        serializer = ProjectSerializer(result_page, many=True)
        response_data["response"] = "Successfully retrieved all projects."
        response_data["data"] = serializer.data
        return paginator.get_paginated_response(response_data)


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer

    def create(self, request):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            response_data["response"] = "Successfully created a new project."
            response_data["name"] = project.name
        else:
            response_data = serializer.errors
        return Response(response_data, status=status.HTTP_201_CREATED)


class ProjectUpdateView(generics.UpdateAPIView):
    serializer_class = ProjectSerializer

    # only owner can update project
    def update(self, request, *args, **kwargs):
        response_data = {}
        project = Project.objects.get(id=kwargs["pk"])
        if project.owner == request.user:
            serializer = self.get_serializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data["response"] = "Successfully updated project."
                response_data["name"] = project.name
            else:
                response_data = serializer.errors
        else:
            response_data["response"] = "You are not the owner of this project."
        return Response(response_data, status=status.HTTP_200_OK)


class ProjectDeleteView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer

    # only owner can delete project
    def delete(self, request, *args, **kwargs):
        response_data = {}
        project = Project.objects.get(id=kwargs["pk"])
        if project.owner == request.user:
            project.delete()
            response_data["response"] = "Successfully deleted project."
            response_data["name"] = project.name
        else:
            response_data["response"] = "You are not the owner of this project."
        return Response(response_data, status=status.HTTP_200_OK)


# ---- Contributor views ----
class ContributorListView(generics.ListAPIView):
    def get(self, request):
        response_data = {}
        contributor = Contributor.objects.all()
        serializer = ContributorGetSerializer(contributor, many=True)
        response_data["response"] = "Successfully retrieved all contributors."
        response_data["data"] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


class ContributorCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contributor = serializer.save()
            response_data["response"] = "Successfully created a new contributor."
            response_data["user"] = contributor.user.username
            response_data["project"] = contributor.project.name
        else:
            response_data = serializer.errors
        return Response(response_data, status=status.HTTP_201_CREATED)
