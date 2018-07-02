from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from posts.form import PostCommentModelForm
from posts.models import Post

__all__ = (
    'post_comment',
)


@require_POST
@login_required
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostCommentModelForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post-list')
