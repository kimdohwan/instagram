from django.contrib.auth import get_user_model
from rest_framework import serializers

from members.serializers import UserSerializer
from .models import Post, PostComment

User = get_user_model()


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'content',
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    # photo = serializers.SerializerMethodField()
    post_comments = PostCommentSerializer()

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'photo',
            'content',
            'created_at',
            'like_users',
            'post_comments',
        )

    # def get_photo(self, post):
    #     request = self.context.get('request')
    #     photo_url = post.photo.url
    #     return request.build_absolute_uri(photo_url)
