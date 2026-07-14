from django.shortcuts import render
from rest_framework import generics
from .serializers import PostDetailSerializer, PostSerializer, CommentSerializer
from .models import Post, Comment
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
# Create your views here.

class PostsApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    pagination_class = PageNumberPagination

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'post_id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


class CommentsApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']

        return Comment.objects.filter(
            post_id=post_id
        ).select_related('author', 'post')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']

        post = get_object_or_404(
            Post,
            id=post_id,
        )

        serializer.save(
            author=self.request.user,
            post=post,
        )


class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'comment_id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        
        return Comment.objects.filter(
            post_id=post_id
        ).select_related('author', 'post')