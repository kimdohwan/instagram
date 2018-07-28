from django.urls import path

from .. import apis
from posts.apis.generic_cbv import PostList as GenericPostList

# app_name = 'apis'
urlpatterns = [
    path('', apis.PostList.as_view(), name='post-list'),
    path('comments/', apis.PostCommentList.as_view(), name='postcomment-list')
    # path('generic-cbv/', GenericPostList.as_view(), name='generic-post-list' )
]
