from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from posts.models import Post

__all__ = (
    'post_like_toggle',
)


@login_required
def post_like_toggle(request, post_pk):
    next_path = request.GET.get('next')
    post = get_object_or_404(Post, pk=post_pk)
    user = request.user

    filtered_like_posts = user.like_posts.filter(pk=post.pk)

    if filtered_like_posts.exists():
        user.like_posts.remove(post)
    else:
        user.like_posts.add(post)

    if next_path:
        return redirect(next_path)

    return redirect('posts:post-list')
