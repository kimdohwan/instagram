from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import PostSerializer
from ..models import Post, PostComment

__all__ = (
    'PostList',
    # 'PostCommentList',
)


# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True, context={"request": request})
#         return Response(serializer.data)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostCommentList(generics.ListCreateAPIView):
#     queryset = PostComment.objects.all()
#     serializer_class = PostCommentSerializer
