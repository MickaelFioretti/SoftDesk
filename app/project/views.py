# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer


# ---- Project views ----
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request):
        response_data = {}
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        response_data["response"] = "Successfully retrieved all projects."
        response_data["data"] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
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


# ---- Contributor views ----
class ContributorListView(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def get(self, request):
        response_data = {}
        contributor = Contributor.objects.all()
        serializer = ContributorSerializer(contributor, many=True)
        response_data["response"] = "Successfully retrieved all contributors."
        response_data["data"] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


class ProjectAddContributorView(generics.CreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def post(self, request, *args, **kwargs):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contributor = serializer.save()
            response_data["response"] = "Successfully created a new contributor."
            response_data["user"] = contributor.user.username
            response_data["project"] = contributor.project.id
        else:
            response_data = serializer.errors
        return Response(response_data, status=status.HTTP_201_CREATED)
