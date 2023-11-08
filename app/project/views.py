# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # get all project and fk of this project but
    def get(
        self,
        request,
    ):
        response_data = {}
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        response_data["response"] = "Successfully retrieved all projects."
        response_data["data"] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


# create project
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            response_data["response"] = "Successfully created a new project."
            response_data["name"] = project.name
        else:
            response_data = serializer.errors
        return Response(response_data, status=status.HTTP_201_CREATED)
