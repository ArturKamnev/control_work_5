
from rest_framework import generics
from .serializers import PostDetailSerializer, PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.


class PostsApiView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Post.objects.select_related('author')

        if self.request.user.is_authenticated:
            return queryset.filter(
                Q(is_published=True) |
                Q(author=self.request.user)
            ).distinct()

        return queryset.filter(is_published=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        queryset = Post.objects.select_related('author')

        if self.request.user.is_authenticated:
            return queryset.filter(
                Q(is_published=True) |
                Q(author=self.request.user)
            ).distinct()

        return queryset.filter(is_published=True)

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