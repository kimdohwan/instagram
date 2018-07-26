from django.urls import path

from posts.apis import PostList
from posts.apis.generic_cbv import PostList as GenericPostList

app_name = 'apis'
urlpatterns = [
    path('posts', PostList.as_view(), name='post-list'),
    # path('generic-cbv/', GenericPostList.as_view(), name='generic-post-list' )
]
