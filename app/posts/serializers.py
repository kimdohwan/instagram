from django.contrib.auth import get_user_model
from rest_framework import serializers

from members.serializers import UserSerializer
from .models import Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'photo',
            'content',
            'created_at',
            'like_users',
        )
