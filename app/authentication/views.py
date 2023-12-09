from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data["response"] = "Successfully registered a new user."
            response_data["username"] = user.username
        else:
            response_data = serializer.errors
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


# ---- User detail view ----
class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.delete()
        response_data = {"response": "Successfully deleted user."}
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
