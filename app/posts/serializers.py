from django.contrib.auth import get_user_model
from rest_framework import serializers

from members.serializers import UserSerializer
from .models import Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    photo = serializers.SerializerMethodField()

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

    def get_photo(self, post):
        request = self.context.get('request')
        photo_url = post.photo.url
        return request.build_absolute_uri(photo_url)
