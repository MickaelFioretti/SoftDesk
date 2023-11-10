# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Project, Contributor
from .serializers import (
    ProjectSerializer,
    ContributorGetSerializer,
)


# ---- Project views ----
class ProjectListView(generics.ListAPIView):
    def get(self, request):
        response_data = {}
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        response_data["response"] = "Successfully retrieved all projects."
        response_data["data"] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


class ProjectCreateView(generics.CreateAPIView):
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
