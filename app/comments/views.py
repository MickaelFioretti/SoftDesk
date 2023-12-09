from rest_framework import generics, status
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsOwner


# ---- Comment views ----
class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_data = {}
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        response_data["response"] = "Successfully retrieved all comments."
        response_data["data"] = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.owner = request.user
            comment = serializer.save()
            response_data["response"] = "Successfully created a new comment."
            response_data["text"] = comment.text
        else:
            response_data = serializer.errors
        return Response(response_data, status=status.HTTP_201_CREATED)


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        response_data = {}
        comment = self.get_object()
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data["response"] = "Successfully updated comment."
            response_data["text"] = serializer.data["text"]
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, *args, **kwargs):
        response_data = {}
        comment = self.get_object()
        comment.delete()
        response_data["response"] = "Successfully deleted comment."
        return Response(response_data, status=status.HTTP_200_OK)


class IssueCommentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, issue_id):
        comments = Comment.objects.filter(issue_id=issue_id).order_by("id")
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
