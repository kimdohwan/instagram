# from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import PostSerializer
from ..models import Post

__all__ = (
    'PostList',
)


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
# return HttpResponse('ggg')
