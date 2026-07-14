from rest_framework import serializers

from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'body',
            'created_at',
            'updated_at',
            'is_published',
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'body',
            'created_at',
            'updated_at',
            'is_published',
        ]


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'body',
            'created_at',
            'updated_at',
            'is_approved',
        ]