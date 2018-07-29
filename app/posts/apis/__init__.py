from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ..pagination import PostListPagination
from ..serializers import PostSerializer
from ..models import Post, PostComment

__all__ = (
    'PostList',
    # 'PostCommentList',
)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostListPagination

# front에서 photo path 를  localhost:3001/media/... 으로 보내서 수정해준 APIview
# 다른 연습하는데 꼬이는 감이 있어서 일단 주석 처리해두고 generic view 사용
# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True, context={"request": request})
#         return Response(serializer.data)


# PostListSerializer 에서 PostComment를 참조하는데 실패한 상태, 일단 주석처리
# class PostCommentList(generics.ListCreateAPIView):
#     queryset = PostComment.objects.all()
#     serializer_class = PostCommentSerializer
