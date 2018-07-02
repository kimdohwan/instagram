from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from posts.models import Post

__all__ = (
    'post_like',
)

@require_POST
@login_required
def post_like(reqeust, pk):
    post = get_object_or_404(Post, pk=pk)
    reqeust.user.like_posts.add(post)
    return redirect('posts:post-detail', pk=pk)