from rest_framework import serializers
from .models import Client, Comment, Likes


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('pk', 'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'text', 'created_at', 'gostos')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ('pk', 'user', 'comment')